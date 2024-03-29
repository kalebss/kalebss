from http import client
import json
import spotipy
import pandas as pd
import config
from flask import flask, redirect, request
from spotipy.oauth2 import SpotifyClientCredentials
import requests


app = flask(book_atx)

# client_id and secret client_id
client_id = config.spotify_client_id
client_secret = config.spotify_secret_id


client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# https://open.spotify.com/playlist/5qiKyBjtLFJyPRDo8RfIiH?si=2ea59ff88bcc460d playlist
playlist_id = "5qiKyBjtLFJyPRDo8RfIiH"
results = sp.playlist(playlist_id)


# create list of song ids
ids = []

for item in results["tracks"]["items"]:
    track = item["track"]["id"]
    ids.append(track)

song_meta = {
    "id": [],
    "album": [],
    "name": [],
    "artist": [],
    "explicit": [],
    "popularity": [],
}

for song_id in ids:
    # get song's meta data
    meta = sp.track(song_id)

    # song id
    song_meta["id"].append(song_id)

    # album name
    album = meta["album"]["name"]
    song_meta["album"] += [album]

    # song name
    song = meta["name"]
    song_meta["name"] += [song]

    # artists name
    s = ", "
    artist = s.join([singer_name["name"] for singer_name in meta["artists"]])
    song_meta["artist"] += [artist]

    # explicit: lyrics could be considered offensive or unsuitable for children
    explicit = meta["explicit"]
    song_meta["explicit"].append(explicit)

    # song popularity
    popularity = meta["popularity"]
    song_meta["popularity"].append(popularity)

song_meta_df = pd.DataFrame.from_dict(song_meta)

# check the song feature
features = sp.audio_features(song_meta["id"])
# change dictionary to dataframe
features_df = pd.DataFrame.from_dict(features)

# convert milliseconds to mins
# duration_ms: The duration of the track in milliseconds.
# 1 minute = 60 seconds = 60 × 1000 milliseconds = 60,000 ms
features_df["duration_ms"] = features_df["duration_ms"] / 60000

# combine two dataframe
final_df = song_meta_df.merge(features_df)

with open(".cache", "r") as f:
    contents = f.read()

data = json.loads(contents)

access_token = data["access_token"]

# define the api endpoint and access token
url = config.spotify_redirect

headers = {"Authorization": f"Bearer {access_token}"}

# make api request
# response = requests.get(url,headers=headers)
response = requests.get(url)

html_content = response.content

with open("response.html", "wb") as f:
    f.write(html_content)
