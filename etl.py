from datetime import date
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import sqlite3

class ETL:

    def __init__(self, player_id, sql_file_path, sql_table_name):
        self.player_id = player_id
        self.sql_file_path = sql_file_path
        self.sql_table_name = sql_table_name
        self.url = f'https://www.unrivaled.basketball/stats/player/{player_id}'
        self.soup = ''
        self.df_info = pd.DataFrame

    def extract(self):
        r = requests.get(self.url)
        self.soup = BeautifulSoup(r.text, 'hmtl.parser')
        if self.soup.find(class_='w-100'):
            return True
        return False
    
    def transform(self):
        player_name = self.soup.find(class_='flex-row items-center w-100 col-8 px-8').find_all('h1')[0]
        player_name = str(player_name)

        #remove html characters from player_name str
        CLEANR = re.compile('<.*?>')
        clean_player_name = re.sub(CLEANR, '', player_name)

        table_html = str(self.soup.find_all('table', class_="w-100 font-13")[0])
        df_info = pd.read_html(table_html)[0]
        cols = df_info.columns.tolist()
        cols.insert(0, 'Date Scrapped')
        cols.insert(1, 'Player Name')
        cols.insert(2, 'PlayerID')
        self.df_info = df_info[cols]

    def load(self):
        with sqlite3.connect(self.sql_file_path) as conn:
            self.df_info.to_sql(self.sql_table_name, conn, if_exists='append', index=False)

    # Class ETL has a run_etl method that runs everthing in the class.
    def run_etl(self):
        if self.extract():
            self.transform()
            self.load()
            print(f'Done with ETL of player_id {self.player_id}')
        else:
            print(f'Skipped player_id {self.player_id}')
