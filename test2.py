import spotipy
import spotipy.util as util

client_id = 'c69d58c04f2441b7a7d6aeaf5bbeb03d'
client_secret = 'cfbccc98451e444e9ed686c9980f5665'
redirect_uri = 'http://localhost'
username = 'mileskidson'

scope = 'user-library-read'

token = util.prompt_for_user_token(username, scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)

if token:
    sp = spotipy.Spotify(auth=token)
    artist_id = 'spotify_artist_id'
    artist = sp.artist(artist_id)
    print(artist['name'])
else:
    print("Can't get token for", username)