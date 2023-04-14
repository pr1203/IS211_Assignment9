import requests
from bs4 import BeautifulSoup

'''This script takes the top 20 artist and prints their name, grammy's won, and number of nominations'''

# Load the webpage content
url = "https://en.wikipedia.org/wiki/List_of_American_Grammy_Award_winners_and_nominees"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")

# Find the table containing the data
table = soup.find("table", class_="wikitable sortable")

# Extract the rows from the table
rows = table.find_all("tr")

# Extract the data for the top 20 artists
data = []
for row in rows[1:21]:  # skip the header row
    cells = row.find_all("td")
    artist = cells[0].get_text()
    wins = cells[1].get_text()
    nominations = cells[2].get_text()
    data.append((artist, wins, nominations))

# Print the data to the screen
print("Top 20 Artists by Wins and Nominations")
for artist, wins, nominations in data:
    print(f"{artist}: {wins} wins, {nominations}nominations")
