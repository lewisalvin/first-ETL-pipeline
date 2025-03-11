import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

import sqlite3
from datetime import date
conn = sqlite3.connect('unrivaled_stats.db')
#c = conn.cursor()

r = requests.get('https://www.unrivaled.basketball/stats/player')
soup = BeautifulSoup(r.text, 'html.parser')
# player_name = soup.find(class_='Player_Player__info--primary__tQjoQ').find_all('h1')[0].find('span')
stat_name = soup.find(class_='p-4 flex-row-to-col-xs justify-between w-100 row-8').find('h2')
table = soup.find_all('table', class_="w-100 font-13")[0]
table_str = str(table)
table_panda = pd.read_html(StringIO(table_str))[0]

cols = table_panda.columns.tolist()
cols.insert(0, 'Date Scrapped')
cols.insert(1, 'Stats')
table_panda['Stats'] = stat_name.text
table_panda['Date Scrapped'] = date.today()
table_panda = table_panda[cols]
#table_panda.to_sql('unrivaled_stats', conn, if_exists='append', index=False)



print(table_panda)