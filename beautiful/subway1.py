# 위키피디아 - 서울 지하철 검색 결과 가져오기
# 가져온 검색결과에서 원하는 부분 추출하기 - 영문사이트

import requests
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

try:
    url = "https://ko.wikipedia.org/wiki/서울_지하철"

    with requests.Session() as s:
        res = s.get(url)

        soup = BeautifulSoup(res.content, "html.parser")

except HTTPError as e:
    print('Http Error')
except URLError as e:
    print('URL Error')
else:
    # 첫번째 이미지 가져오기
    image1 = soup.select_one(
        "#mw-content-text > div > table.infobox > tbody > tr:nth-child(1) > td > a > img")
    print(image1)
    # 두번째 이미지 가져오기
    print("\n두번째 이미지")

    image2 = soup.select_one(
        "#mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img")
    print(image2)

    # image1 의 src 출력
    print("image1 src : ", image1["src"])
    print("image2 src : ", image2["src"])

    print()
    # a 링크의 갯수는 몇개?
    links = soup.select("a")
    print("link count : ", len(links))

    # a 링크에서 클래스명이 external text 찾기
    external = soup.select("a[class='external text']")
    print(external[:3])
