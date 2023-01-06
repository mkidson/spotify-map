import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# export SPOTIPY_CLIENT_ID='c69d58c04f2441b7a7d6aeaf5bbeb03d'
# export SPOTIPY_CLIENT_SECRET='cfbccc98451e444e9ed686c9980f5665'

auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

playlist = sp.playlist('https://open.spotify.com/playlist/6m6R5pBbyLkKEwjVLXT8iP?si=b2fcf1bfcff444d4')

print(playlist)

# while playlists:
#     for i, playlist in enumerate(playlists['items']):
#         print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
#     if playlists['next']:
#         playlists = sp.next(playlists)
#     else:
#         playlists = None