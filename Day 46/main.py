from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
year_interest = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{year_interest}/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}

response = requests.get(BILLBOARD_URL, headers=header)
content = response.text

soup = BeautifulSoup(content,"html.parser")
my_playlist = [song.getText().strip() for song in soup.select("li ul li h3")]

# Spotify
spotify = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt"))

user_id = spotify.current_user()['id']

year = year_interest.split("-")[0]
song_uris = []
for song in my_playlist:
    result = spotify.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify, Skipped.")

# Create the sportify playlist
playlist = spotify.user_playlist_create(user=user_id, name=f"{year_interest} Billboard 100", public="False")
print(playlist)

# Adding songs found into the new playlist
spotify.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
