import requests
from bs4 import BeautifulSoup


def get_billboard_data(query_date):
    """Scrape Billboard Hot 100 data for a given date."""

    url = f"https://www.billboard.com/charts/hot-100/{query_date}"

    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve Billboard data: {e}")
        return [], []

    soup = BeautifulSoup(response.text, "html.parser")

    # Extract the artist names and song titles from the specified <div> elements
    billboard_chart_titles = soup.find_all("div", class_="o-chart-results-list-row-container")
    song_titles_list = [div_element.find("h3").getText().strip() for div_element in billboard_chart_titles]

    billboard_chart_artists = soup.select("li ul li span.a-no-trucate")
    artists_list = [span_tag.getText().strip() for span_tag in billboard_chart_artists]

    return song_titles_list, artists_list


if __name__ == "__main__":
    query_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")
    song_titles, artists = get_billboard_data(query_date)

    if song_titles and artists:
        print("Song Titles:", song_titles)
        print("Artists:", artists)
    else:
        print("No data retrieved.")
