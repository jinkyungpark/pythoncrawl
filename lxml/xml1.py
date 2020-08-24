import requests
from urllib.error import HTTPError
from lxml import etree


def main():
    # 가져올 rss 주소
    url = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001'

    try:

        with requests.Session() as r:

            res_data = r.get(url)
            # print(res_data.text)
            parseData(res_data)

    except HTTPError as e:
        print(e)


def parseData(res_data):
    # url로부터 받은 데이터를 etree 구조로 변경
    # byte 형태의 input을 하라고 함
    #root = etree.fromstring(res_data.content)
    root = etree.XML(res_data.content)  # 이렇게 해도 fromstring()과 같은 역할
    print(root)  # rss
    print(type(root))  # <class 'lxml.etree._Element'>
    print(root.tag)  # root 태그 찾기

    # root 태그 아래 child 태그 찾기
    children = root[0]
    print("child.tag", children.tag)
    print(root.find("channel").tag)
    print()

    # channel 태그 아래 있는 모든 자식 태그 가져오기
    for child in children:
        print(child.tag, " : ", child.text)
        for ch in child:
            print(ch.tag, ":", ch.text)


if __name__ == "__main__":
    main()
