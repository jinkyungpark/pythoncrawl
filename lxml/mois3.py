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
        print(root)
        print(type(root))  # <class 'lxml.etree._Element'>
        print(root.tag)  # root 태그 찾기

        # root 태그 아래 child 태그 찾기
        child = root[0]
        print("child.tag", child.tag)
        print(root.find("channel").tag)
        print()

        # channel 태그 아래 있는 모든 자식 태그 가져오기
        for ch in child:
            print(ch.tag, " : ", ch.text)

    except HTTPError as e:
        print(e)


if __name__ == "__main__":
    parseData()
