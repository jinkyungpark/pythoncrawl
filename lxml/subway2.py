# 위키피디아 - 서울 지하철 검색 결과 가져오기
# 가져온 검색결과에서 원하는 부분 추출하기 - 한글사이트

import requests
from lxml.html import fromstring, tostring
from urllib.error import HTTPError, URLError

try:
    url = "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0"
    with requests.Session() as s:
        res = s.get(url)
        data = fromstring(res.content)  # 문자열 저장
except HTTPError as e:
    print('Http Error')
except URLError as e:
    print('URL Error')
else:
    # 저장된 문자열에서 원하는 태그 찾기
    for a in data.xpath('//*[@id="mw-content-text"]/div/table/tbody/tr/td/a/img'):
        print(tostring(a, pretty_print=True))

    # 이미지 태그 내에서 src 만 가지고 오고 싶었다면?
    print("-----------------")
    print(data.xpath(
        '//*[@id="mw-content-text"]/div/table/tbody/tr/td/a/img/@src'))
    print()

    # css select 로 가져온다면?
    print("*****************")
    # #mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img
    for a in data.cssselect('div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img'):
        # 전체 태그
        print(tostring(a, pretty_print=True))

        # href 속성
        print("{}".format(a.get("src")))
