import requests
from lxml.html import fromstring, tostring


def main():
    res = requests.get("https://www.naver.com")
    # 신문사 링크 리스트 얻기
    urls = scrape_news_list_page(res)

    # 링크 리스트 파일 저장하기
    for name, url in urls.items():
        print(name, url)
        with open("d:/download/link1.txt", "a") as f:
            f.write(name + " : " + url + "\n")


def scrape_news_list_page(res):
    # 파싱 구조로 변경
    root = fromstring(res.content)

    urls = {}

    for a in root.cssselect("div.thumb_area div.thumb_box"):
        name, url = extract_contents(a)
        urls[name] = url
    return urls


def extract_contents(a):
    # 주소 추출
    link = a.cssselect(".popup_wrap a:nth-child(3)")
    link = link[0].get("href")

    # 회사명 추출
    name = a.cssselect("img")[0].get("alt")
    print(name)
    return name, link


if __name__ == "__main__":
    main()

