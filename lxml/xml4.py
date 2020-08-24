import requests
from lxml.html import fromstring, tostring


def parseData():
    # 가져올 rss 주소
    url = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1013'

    try:

        with requests.Session() as r:

            res_data = r.get(url)
            print(res_data.text)

        # byte 형태의 input을 하라고 함
        root = fromstring(res_data.content)
        print(root)
        print(type(root))  # <class 'lxml.html.HtmlElement'>

        # title 태그를 찾아서 그 안의 text 출력하기
        title = root.cssselect("title")
        print(type(title))  # <class 'list'>
        print(title[0].text_content())

        # 태그 안 내용들만 전체 출력
        print(root.text_content())  # lxml.html 로 할 때만 사용 가능
        # byte 형태로 출력
        print(tostring(root))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    parseData()
