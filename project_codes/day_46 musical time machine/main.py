from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
import os


top100_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{top100_date}/")
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
songs = soup.select(selector="li h3#title-of-a-story")
top_100 = [song.getText().strip() for song in songs]
# pprint(top_100)

# Authenticate app with spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ.get("SPOTIFY_ID"),
    client_secret=os.environ.get("SECRET"),
    redirect_uri="http://example.com",
    scope="playlist-modify-private",
))

user_profile = sp.current_user()
user_id = user_profile["id"]

# search for the songs' URI
year = top100_date.split("-")[0]
song_URIs = []
for song in top_100:
    result = sp.search(q=f'track: {song} year: {year}', type="track")
    try:
        song_URIs.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")
# pprint(song_URIs)

# create a playlist and add songs that I scraped using their URI
name_playlist = f"{top100_date} Billboard 100"
playlist = sp.user_playlist_create(user=user_id, name=name_playlist, public=False, description="Top 100 songs on"
                                                                                               f" {top100_date}")
playlist_id = playlist["id"]
add_songs = sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=song_URIs)
print("\ndone")
