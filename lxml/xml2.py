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
    # print(root)  # rss
    # print(type(root))  # <class 'lxml.etree._Element'>
    # print("root tag : {}".format(root.tag))  # root 태그 찾기

    # root 태그 아래 child 태그 찾기
    channel = root.xpath("//channel")
    print(channel[0].tag)

    # root 태그 아래 link 태그 찾아서 텍스트 가져오기
    print("\nroot 태그 아래 link 태그 텍스트 출력")
    link1 = root.xpath("//link/text()")
    print(link1)

    # root 태그 아래 title 태그 찾아서 텍스트 가져오기
    print("\nroot 태그 아래 title 태그 텍스트 출력")
    title = root.xpath("//title/text()")
    print(title)

    # item 가져오기
    print("\n")
    items = root.xpath("//channel/item")
    for item in items:
        for data in item:
            print(data.tag, ":", data.text)
        print("\n")


if __name__ == "__main__":
    main()
