from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, MusicPreference
from .serializers import UserSerializer, MusicPreferenceSerializer
from spotify_api.views import get_spotify_token
import requests

# -------------------------------
# CRUD de usuarios
# -------------------------------
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# -------------------------------
# CRUD de preferencias musicales
# -------------------------------
class MusicPreferenceViewSet(viewsets.ModelViewSet):
    queryset = MusicPreference.objects.all()
    serializer_class = MusicPreferenceSerializer

    def perform_create(self, serializer):
        """
        Al crear una preferencia:
        - Llama a Spotify
        - Obtiene top tracks automáticamente
        - Guarda la preferencia con top_tracks
        """
        artist = serializer.validated_data["artist"]
        user = serializer.validated_data["user"]

        # Obtener token de Spotify
        token = get_spotify_token()
        headers = {"Authorization": f"Bearer {token}"}

        # Buscar artista
        search_resp = requests.get(
            "https://api.spotify.com/v1/search",
            headers=headers,
            params={"q": artist, "type": "artist", "limit": 1}
        )

        artists = search_resp.json().get("artists", {}).get("items", [])
        top_tracks = []

        if artists:
            artist_id = artists[0]["id"]

            # Obtener top tracks
            top_resp = requests.get(
                f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks",
                headers=headers,
                params={"market": "US"}
            )
            top_tracks = [t["name"] for t in top_resp.json().get("tracks", [])]

        # Guardar la preferencia con top_tracks
        serializer.save(top_tracks=top_tracks)


# -------------------------------
# Endpoint opcional solo para consultar Spotify sin guardar
# -------------------------------
class SpotifyViewSet(viewsets.ViewSet):
    """
    Buscar un artista y obtener top tracks sin guardar nada en DB
    """
    def list(self, request):
        artist = request.query_params.get("artist")

        if not artist:
            return Response(
                {"error": "Debe enviar el parámetro artist"},
                status=status.HTTP_400_BAD_REQUEST
            )

        token = get_spotify_token()
        headers = {"Authorization": f"Bearer {token}"}

        # Buscar artista
        search_resp = requests.get(
            "https://api.spotify.com/v1/search",
            headers=headers,
            params={"q": artist, "type": "artist", "limit": 1}
        )

        artists = search_resp.json().get("artists", {}).get("items", [])
        if not artists:
            return Response({"error": "Artista no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        artist_info = artists[0]

        # Top tracks
        top_resp = requests.get(
            f"https://api.spotify.com/v1/artists/{artist_info['id']}/top-tracks",
            headers=headers,
            params={"market": "US"}
        )
        top_tracks = [t["name"] for t in top_resp.json().get("tracks", [])]

        return Response({
            "artist": artist_info["name"],
            "top_tracks": top_tracks
        })

