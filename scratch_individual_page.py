import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.wnba.com/player/1628932')
soup = BeautifulSoup(r.text, 'html.parser')
player_name = soup.find(class_='Player_Player__info--primary__tQjoQ').find_all('h1')[0].find('span')

print(r.text)