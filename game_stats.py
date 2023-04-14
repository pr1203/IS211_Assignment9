import requests
from bs4 import BeautifulSoup

'''this script prints the top 20 games and prints the title, number of downloads, and date released'''

url = "https://en.wikipedia.org/wiki/List_of_most-played_video_games_by_player_count"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")
table = soup.find("table", {"class": "wikitable sortable"})
rows = table.find_all("tr")[1:]

count = 0
for row in rows:
    cells = row.find_all("td")
    game_name = cells[0].text.strip()
    downloads = cells[1].text.strip()
    release_date = cells[2].text.strip()
    print(f"{game_name} - {downloads} downloads - Released: {release_date}")
    count += 1
    if count == 20:
        break

''' pip install request & pip install beautifulsoup4 required to run'''
