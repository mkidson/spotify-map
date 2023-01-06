import requests

access_token = 'your_access_token'
artist_id = 'spotify_artist_id'

headers = {
    'Authorization': 'Bearer ' + access_token
}

response = requests.get(f'https://api.spotify.com/v1/artists/{artist_id}', headers=headers)

artist = response.json()
print(artist['name'])