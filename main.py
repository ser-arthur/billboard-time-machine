import spotipy
from spotipy import SpotifyException
from spotipy.oauth2 import SpotifyOAuth
from billboard_scraper import get_billboard_data


def create_spotify_playlist(query_date):
    """Creates a Spotify playlist with Billboard Hot 100 songs for a given date (YYYY-MM-DD)."""

    query_year = query_date.split("-")[0]
    scope = "playlist-modify-private"
    playlist_data = {
        "name": f"{query_date} Billboard 100",
        "description": f"Hit songs from the {query_year} era.",
        "public": False,
    }

    # Authenticate user with Spotipy
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    user_info = sp.current_user()
    user_id = user_info["id"]

    # Create a private playlist with Spotipy
    playlist = sp.user_playlist_create(
        user=user_id,
        name=playlist_data["name"],
        description=playlist_data["description"],
        public=playlist_data["public"],
    )
    playlist_id = playlist["id"]

    # Get song titles and artists from Billboard
    song_titles_list, artists_list = get_billboard_data(query_date)
    song_uris = []

    for title, artist in zip(song_titles_list, artists_list):
        # First search query: with title, artist, and year
        query = f"track:{title} artist:{artist} year:{query_year}"

        try:
            search_result = sp.search(query, type="track")
            track = search_result["tracks"]["items"]

            if not track:
                print(
                    f"No track found with the title: {title} by artist: {artist}. Trying simpler search..."
                )

                # Fallback search query: with title only
                fallback_query = f"track:{title}"
                fallback_search_result = sp.search(fallback_query, type="track")
                fallback_track = fallback_search_result["tracks"]["items"]

                if not fallback_track:
                    print(
                        f"No track found with the title: {title} even with simpler search."
                    )
                    continue

                print(
                    f"Track found using simpler search: {fallback_track[0]['name']} by "
                    f"{fallback_track[0]['artists'][0]['name']}"
                )

                # Get URI for the existing track from the fallback search
                track_uri = fallback_track[0]["uri"]
            else:
                # Get URI for the existing track from the detailed search
                track_uri = track[0]["uri"]

            song_uris.append(track_uri)

        except SpotifyException as se:
            print(f"Spotify exception occurred: {se}")
        except Exception as e:
            print(f"An exception occurred: {type(e).__name__} - {str(e)}")

    # Add songs to the playlist
    if song_uris:
        sp.playlist_add_items(playlist_id, song_uris)
        print(f"Playlist created successfully with {len(song_uris)} tracks.")
    else:
        print("No tracks added to the playlist.")


if __name__ == "__main__":
    query_date = input(
        "Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n"
    )
    create_spotify_playlist(query_date)
