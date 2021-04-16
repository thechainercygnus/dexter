from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def find_tracks_by_artist(search_term):
    spotifyclient = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=getenv('SPOTIFY_ID'),client_secret=getenv('SPOTIFY_SECRET')))
    results = spotifyclient.search(q=search_term,limit=5)
    return results

def find_similar_artists(search_term):
    spotifyclient = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=getenv('SPOTIFY_ID'),client_secret=getenv('SPOTIFY_SECRET')))
    artist_info = spotifyclient.search(q=search_term,type='artist')
    artist_id = artist_info['artists']['items'][0]['id']
    full_results = spotifyclient.artist_related_artists(artist_id)
    return full_results