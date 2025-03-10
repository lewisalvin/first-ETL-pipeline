import requests
from bs4 import BeautifulSoup
import pandas as pd

r = requests.get('https://www.unrivaled.basketball/stats/player')

soup = BeautifulSoup(r.text, 'html.parser')

# player_name = soup.find(class_='Player_Player__info--primary__tQjoQ').find_all('h1')[0].find('span')

table = soup.find_all('table', class_="w-100 font-13")[0]

table_str = str(table)

table_panda = pd.read_html(table_str)



print(table_panda)