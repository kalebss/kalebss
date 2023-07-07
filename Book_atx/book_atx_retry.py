from http import client
import json
import spotipy
import pandas as pd
import config
from flask import Flask, redirect, request, jsonify
from spotipy.oauth2 import SpotifyClientCredentials
from requests import post, get
import base64


app = Flask(__name__)

# client_id and secret client_id
client_id = config.spotify_client_id
client_secret = config.spotify_secret_id
playlist_id = "5qiKyBjtLFJyPRDo8RfIiH"


client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded",
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_results = json.loads(result.content)
    token = json_results["access_token"]
    return token


def get_auth_header(token):
    return {"Authorization": "Bearer " + token}


def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)


def search_for_playlist(token, playlist_id):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={playlist_id}&type=playlist"

    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)
    print(json_result)


token = get_token()
search_for_artist(token, "ODESZA")
search_for_playlist(token, playlist_id)


# # # https://open.spotify.com/playlist/5qiKyBjtLFJyPRDo8RfIiH?si=2ea59ff88bcc460d playlist
# # results = sp.playlist(playlist_id)


# # # create list of song ids
# # ids = []

# # for item in results["tracks"]["items"]:
# #     track = item["track"]["id"]
# #     ids.append(track)

# # song_meta = {
# #     "id": [],
# #     "album": [],
# #     "name": [],
# #     "artist": [],
# #     "explicit": [],
# #     "popularity": [],
# # }

# # for song_id in ids:
# #     # get song's meta data
# #     meta = sp.track(song_id)

# #     # song id
# #     song_meta["id"].append(song_id)

# #     # album name
# #     album = meta["album"]["name"]
# #     song_meta["album"] += [album]

# #     # song name
# #     song = meta["name"]
# #     song_meta["name"] += [song]

# #     # artists name
# #     s = ", "
# #     artist = s.join([singer_name["name"] for singer_name in meta["artists"]])
# #     song_meta["artist"] += [artist]

# #     # explicit: lyrics could be considered offensive or unsuitable for children
# #     explicit = meta["explicit"]
# #     song_meta["explicit"].append(explicit)

# #     # song popularity
# #     popularity = meta["popularity"]
# #     song_meta["popularity"].append(popularity)

# # song_meta_df = pd.DataFrame.from_dict(song_meta)

# # # check the song feature
# # features = sp.audio_features(song_meta["id"])
# # # change dictionary to dataframe
# # features_df = pd.DataFrame.from_dict(features)

# # # convert milliseconds to mins
# # # duration_ms: The duration of the track in milliseconds.
# # # 1 minute = 60 seconds = 60 × 1000 milliseconds = 60,000 ms
# # features_df["duration_ms"] = features_df["duration_ms"] / 60000

# # # combine two dataframe
# # final_df = song_meta_df.merge(features_df)

# # @app.route('/api/spotify', methods=['GET'])
# # def get_spotify_data():
# #     # Spotify API URL
# #     url = 'https://api.spotify.com/v1/albums/0sNOF9WDwhWunNAHPD3Baj'

# #     # Create the headers
# #     headers = {
# #         'Accept': 'application/json',
# #         'Content-Type': 'application/json',
# #         'Authorization': f'Basic {CLIENT_ID}:{CLIENT_SECRET}',
# #     }

# #     # Make the request
# #     response = requests.get(url, headers=headers)

# #     # Parse the response
# #     if response.status_code == 200:
# #         data = response.json()
# #         return jsonify(data), 200
# #     else:
# #         return jsonify({'message': 'Error occurred'}), response.status_code

# # if __name__ == "__main__":
# #     app.run(debug=True)
