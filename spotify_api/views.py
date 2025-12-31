import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings

def get_spotify_token():
    url = "https://accounts.spotify.com/api/token"
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, data=data, auth=(settings.SPOTIFY_CLIENT_ID, settings.SPOTIFY_CLIENT_SECRET))
    response.raise_for_status()
    return response.json()["access_token"]

class SpotifySearchView(APIView):

    def get(self, request):
        artist = request.query_params.get('artist')
        if not artist:
            return Response({"error": "Debes enviar el parámetro 'artist'"}, status=400)

        token = get_spotify_token()
        headers = {"Authorization": f"Bearer {token}"}

        # Buscar artista
        search_url = "https://api.spotify.com/v1/search"
        params = {"q": artist, "type": "artist", "limit": 1}
        search_resp = requests.get(search_url, headers=headers, params=params)
        if search_resp.status_code != 200:
            return Response({"error": "Error al consultar Spotify"}, status=500)

        artists = search_resp.json().get("artists", {}).get("items", [])
        if not artists:
            return Response({"error": "Artista no encontrado"}, status=404)

        artist_info = artists[0]

        # Top tracks
        top_url = f"https://api.spotify.com/v1/artists/{artist_info['id']}/top-tracks"
        top_resp = requests.get(top_url, headers=headers, params={"market": "US"})
        top_tracks = [t["name"] for t in top_resp.json().get("tracks", [])]

        return Response({
            "artist": artist_info["name"],
            "top_tracks": top_tracks
        })

