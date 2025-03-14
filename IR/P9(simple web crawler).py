import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/States_and_union_territories_of_India'

res = requests.get(URL).text
soup = BeautifulSoup(res, 'lxml')
states = []

table = soup.find('table', class_='wikitable')
if table:
    for items in table.find_all('tr')[1:]:
        data = items.find_all(['th', 'td'])
        if data:
            states.append(data[0].text.strip())

print(states)