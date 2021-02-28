# 네이트 가장 많이 본 뉴스
# 시사 5개 가져오기

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import xlsx_write as excel


url = "https://news.nate.com/rank/interest?sc=sisa&p=day&date=20210228"
try:
    html = requests.get(url)
except HTTPError as e:
    print("HTTP Error", e)
try:
    soup = BeautifulSoup(html.content, "html.parser")
    # #newsContents > div > div.postRankSubjectList.f_clear >
    #  div:nth-child(1) > div > a > span.tb > strong
    news_list = soup.select(
        "div.mduSubjectList.f_clear > div > a > span.tb > strong")
    print(news_list)
except AttributeError as e:
    print("tag was not found")

# 전체 소스에서 내용 선택
news_lists = list()
for i, news in enumerate(news_list, 1):
    print()
    print("{} : {}".format(i, news.text))
    news_lists.append([news.string])


# 엑셀저장
excel.write_excel_template("210228.xlsx", "시사", news_lists)
