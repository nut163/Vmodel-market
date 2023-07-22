```python
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# User Data Schema
from user_data_schema import UserData

# Message Names
from message_names import spotifyLinkSuccess

# DOM Element IDs
from dom_element_ids import spotifyLinkButton

# Function Names
from function_names import linkSpotify

def spotify_integration(user: UserData):
    scope = "user-read-private user-read-email"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    # Link Spotify account to user profile
    def link_spotify():
        try:
            results = sp.current_user()
            user.spotify_profile = results['external_urls']['spotify']
            print(spotifyLinkSuccess)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # Event listener for Spotify link button
    def on_spotify_link_button_click(event):
        link_spotify()

    # Bind the event listener to the Spotify link button
    spotifyLinkButton.bind("<Button-1>", on_spotify_link_button_click)
```