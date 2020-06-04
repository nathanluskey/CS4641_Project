from secrets import secrets
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#for os information look at https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
os.environ["SPOTIPY_CLIENT_ID"] = secrets.SPOTIPY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = secrets.SPOTIPY_CLIENT_SECRET
# on MAC, use `export` on Windows use 'set'


#Taken from https://github.com/plamere/spotipy
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])