from django.urls import path
from .views import SpotifySearchView

urlpatterns = [
    path('search/', SpotifySearchView.as_view(), name='spotify-search'),
]
