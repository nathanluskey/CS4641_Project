from secrets import secrets
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#imports for a GUI if you want
# import tkinter as tk
# from tkinter import simpledialog

#for os information look at https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
os.environ["SPOTIPY_CLIENT_ID"] = secrets.SPOTIPY_CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"] = secrets.SPOTIPY_CLIENT_SECRET

#Taken from https://github.com/plamere/spotipy
sp = spotipy.Spotify(client_credentials_manager = SpotifyClientCredentials())

# For a GUI if you want
# application_window = tk.Tk()
# answer = simpledialog.askstring("Input", "Enter the URL of your favorite spotify playlist", parent=application_window)
answer = "spotify:playlist:37i9dQZF1DWZreqadA03A8"


nathanPlaylist = sp.playlist(answer)
#This is a python dict, so use .keys() repeatedly to find what we want

#Printing out the first song of a playlist
#firstSong = nathanPlaylist['tracks']['items'][0]['track']['name']

#This loop prints all song names in a playlist
for i in nathanPlaylist["tracks"]["items"]:
    try:
        songName = i["track"]["name"]
        print(songName)
    except Exception as e:
        print(e)