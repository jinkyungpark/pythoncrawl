# lxml 사용 기초 스크랩핑(2)
import requests
from lxml.html import fromstring, tostring  # 전체 라이브러리보다는 사용할 모듈만 가져오기


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인 함수
    """

    # 세션 사용
    session = requests.Session()

    # 스크랩핑 대상 URL

    # response = req.urlopen("https://www.naver.com")
    # contents = response.read()
    # 해서 가져왔던 부분을 reqeusts를 쓰면 편하게 가져올 수 있으며 뒤의 get(), post() 함수로 어떤 방식
    # 으로 가져올 것인지 처리

    response = session.get("https://www.naver.com")

    # 신문사 링크 딕셔너리 획득(신문사 이름과 정보 가져오기)
    urls = scrape_news_list_page(response)

    # 딕셔너리 확인
    # print(urls)

    # 결과 출력
    for name, url in urls.items():
        print(name, url)
        # 파일쓰기
        with open('c:/download/result.txt', 'a') as c:
            c.write(name+' : '+url+"\n")   # 엔터 포함


def scrape_news_list_page(res):
    # url 딕셔너리 선언
    urls = {}

    # 태그 정보 문자열 저장
    root = fromstring(res.content)

    for a in root.xpath('//ul[@class="api_list"]/li[@class="api_item"]/a[@class="api_link"]'):
        # a 구조확인
        # print(a)

        # a 문자열 확인
        # print(tostring(a, pretty_print=True))

        name, url = extract_contents(a)

        # 딕셔너리 삽입
        urls[name] = url

    return urls


def extract_contents(dom):
    # 링크 주소
    link = dom.get("href")

    # 신문사명
    name = dom.xpath("./img")[0].get('alt')
    return name, link


# 스크랩핑 시작
if __name__ == "__main__":
    main()
