# 네이버 가장 많이 본 뉴스
# 정치 10개 가져오기

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError


url = "https://news.naver.com/"
try:
    html = requests.get(url)
except HTTPError as e:
    print("HTTP Error", e)
try:
    soup = BeautifulSoup(html.content, "html.parser")
    news_list = soup.select(
        "div#ranking_100 > ul.section_list_ranking > li > a")
except AttributeError as e:
    print("tag was not found")

# 전체 소스에서 내용 선택
for i, news in enumerate(news_list, 1):
    print()
    print("{} : {}".format(i, news['title']))


