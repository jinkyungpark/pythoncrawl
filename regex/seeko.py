from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

for index in range(1, 2):
    res = urlopen(
        'https://seeko.earlyadopter.co.kr/bbs/board.php?bo_table=mainnews&page='+str(index))
    soup = BeautifulSoup(res, 'html.parser')

    data = soup.find_all('td', 'article_subject')
    for item in data:
        print(item.get_text())
