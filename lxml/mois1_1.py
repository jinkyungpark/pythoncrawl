import requests
import lxml.html
import cssselect


def parseData():
    # 가져올 rss 주소
    url = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1011'

    try:

        with requests.Session() as r:

            res_data = r.get(url)
            print(res_data.text)

        # byte 형태의 input을 하라고 함
        root = lxml.html.fromstring(res_data.content)

        for item in root.cssselect("channel"):
            for child in item.getchildren():
                print(child.tag, "=>", child.text_content())

    except Exception as e:
        print(e)


if __name__ == "__main__":
    parseData()
