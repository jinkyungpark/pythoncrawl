import requests
from urllib.error import HTTPError
from lxml import etree

# 행정 안전부 : https://www.mois.go.kr


def parseData():
    # 가져올 rss 주소
    url = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1013'

    try:

        with requests.Session() as r:

            res_data = r.get(url)

        root = etree.fromstring(res_data.content)  # byte 형태의 input을 하라고 함

        # channel 아래에 있는 자식 태그 가져와서 text 만 출력하기
        for ele in root.find("channel").getchildren():
            if not ele.text:
                text = "None"
            else:
                text = ele.text
            print(ele.tag, "=>", text)

        # print(etree.tostring(root))

    except HTTPError as e:
        print(e)


if __name__ == "__main__":
    parseData()
