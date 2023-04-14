import requests
from bs4 import BeautifulSoup

'''outputs the list of top 20 players, including the player’s position, team and total number of touchdowns'''

url = 'https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending'

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find_all('table')[0]

rows = table.find_all('tr')[1:21]

print("Top 20 Players by Touchdowns:\n")

for row in rows:
    data = row.find_all('td')
    player = data[0].text.strip()
    position = data[1].text.strip()
    team = data[2].text.strip()
    touchdowns = data[8].text.strip()
    print(f"{player} ({position}, {team}): {touchdowns} touchdowns")

'''must run pip install requests in terminal'''
'''must run pip install bs4 in terminal'''
