# Billboard Time Machine

This project helps you easily create Spotify playlists based on the Billboard Hot 100 charts from any date in the past. Using the Spotify API and web scraping, it pulls together playlists that take you back to the top songs from any specific date. Perfect for reliving your favorite music eras or discovering what was trending back in the day.

## How It Works

1. Scrapes Billboard Hot 100 for a given date (YYYY-MM-DD). (`billboard_scraper`)
2. Searches Spotify for each song and creates a playlist with matching tracks. (`main.py`)

## Features

- Web scraping via BeautifulSoup
- Spotify API interaction using Spotipy

## Getting Started

To tap into the Spotify Web API, your app needs to be authenticated. Direct authentication with Spotify can be a little tricky, so we use **Spotipy** instead. Spotipy simplifies the authentication process and manages all communications with the Spotify Web API.

## Authentication

1. **Spotify Account & App**: Create a Spotify account and app on the Spotify Developer Dashboard to obtain a Client ID and Secret.

2. **Set Environment Variables**: Store your `Client ID` and `Secret` as environment variables.

3. **Run the Script**: Upon running the script, your web browser will open the Spotify login page. Log in and authorize the app, and Spotify will redirect you to a URL. Copy this URL and paste it into your terminal. A cache file storing your authentication token will be created, allowing the app to interact with the Spotify API without needing to re-authenticate for future requests.

## Troubleshooting

- Ensure environment variables (`Client ID/Secret`) are set correctly.
- Making too many requests to the API may result in the search returning a single random song. You can avoid this by pausing between requests.

## Run
- Launch the project with `main.py`.

## Author
**Kobby S. Arthur**
