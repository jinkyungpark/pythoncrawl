from lxml.html import tostring, fromstring
import requests


def main():
    # 네이버 뉴스 기사
    url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=366&aid=0000576630"

    with requests.Session() as s:
        response = s.get(url)

        data_extract(response)


def data_extract(response):
    # lxml.html 이 파싱을 할 수 있도록 문서 구조 생성하기
    html_ele = fromstring(response.text)
    print(html_ele)  # <Element html at 0x263bf2c8090>

    # 신문기사 타이틀 출력하기
    titles = html_ele.cssselect("#articleTitle")
    print("title type : {}".format(type(titles)))
    print(titles[0].text)
    for title in titles:
        print(title.text)
        print(title.text_content())


if __name__ == "__main__":
    main()
