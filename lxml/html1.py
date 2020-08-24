from lxml import etree
from lxml.html import tostring, fromstring
import requests


def main():
    # 네이버 뉴스 기사
    url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=366&aid=0000576630"

    # lxml 이 파싱을 할 수 있도록 문서 구조 생성하기
    with requests.Session() as s:
        response = s.get(url)

        data_extract(response)


def data_extract(response):
    html_ele = fromstring(response.text)
    print(html_ele)  # <Element html at 0x263bf2c8090>


if __name__ == "__main__":
    main()
