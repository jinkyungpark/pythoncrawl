import requests
from urllib.error import HTTPError
from lxml import etree


def parseData():
    # 가져올 rss 주소
    url = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1013'

    try:

        with requests.Session() as r:

            res_data = r.get(url)
            print(res_data.text)

        # url로부터 받은 데이터를 etree 구조로 변경
        # byte 형태의 input을 하라고 함
        root = etree.fromstring(res_data.content)

        # root 태그 아래 link 태그 찾아서 텍스트 가져오기
        link1 = root.xpath("//link/text()")
        print(link1)

        # root 태그 아래 title 태그 찾아서 텍스트 가져오기
        title = root.xpath("//title/text()")
        print(title[0])

        print(etree.tostring(root))

    except HTTPError as e:
        print(e)


if __name__ == "__main__":
    parseData()
