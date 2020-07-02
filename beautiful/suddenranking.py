import requests
from bs4 import BeautifulSoup


res = requests.get(
    'https://datalab.naver.com/keyword/realtimeList.naver?datetime=2020-07-01T21%3A32%3A00')
soup = BeautifulSoup(res.content, 'html.parser')

print(soup)
