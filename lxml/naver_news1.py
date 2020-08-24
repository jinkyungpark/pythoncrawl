# lxml 사용 기초 스크랩핑(1)
import requests
import lxml.html


def main():
    """
    네이버 메인 뉴스 스탠드 스크랩핑 메인 함수
    """
    # 스크랩핑 대상 URL

    # response = req.urlopen("https://www.naver.com")
    # contents = response.read()
    # 해서 가져왔던 부분을 reqeusts를 쓰면 편하게 가져올 수 있으며 뒤의 get(), post() 함수로 어떤 방식
    # 으로 가져올 것인지 처리

    response = requests.get("https://www.naver.com")
    # print(response)  # <Response [200]>
    # print(response.text)   # 가져온 페이지 전체 출력
    # print(response.text[:1000])  # 1000개만 가져오기
    # print(response.content[:1000])  # 1000개만 가져오기

    # 신문사 링크 리스트 획득
    urls = scrape_news_list_page(response)
    for url in urls:
        print(url)
        # 파일쓰기
        with open('c:/download/result.txt', 'a') as c:
            c.write(url+"\n")   # 엔터 포함


def scrape_news_list_page(res):
    # url 리스트 선언
    urls = []

    # 태그 정보 문자열 저장
    root = lxml.html.fromstring(res.content)
    # print(root)   #<Element html at 0x1fd32433180>

    # html로 온 문서에 대해서 css 선택자로 원하는 부분 찾기(동강)
    # cssselect 는 설치한 라이브러리에서 가져옴
    # for a in root.cssselect('.api_list .api_item a.api_link'):
    #     # 링크
    #     url = a.get('href')
    #     urls.append(url)
    # return urls

    # 06/10 확인시 변경됨
    for a in root.cssselect('.thumb_area > .thumb_box > div.popup_wrap > a:nth-child(3)'):
        # 링크
        url = a.get('href')
        urls.append(url)
    return urls


# 스크랩핑 시작
if __name__ == "__main__":
    main()
