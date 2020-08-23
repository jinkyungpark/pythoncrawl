import requests
from lxml import etree  # 파생을 위해

# 기상청에서 오늘의 날씨 중 서울.경기도 RSS


def parseData():
    try:

        weather_url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'
        weather_dict = {}
        weathers = []
        with requests.Session() as s:
            data = s.get(weather_url)

            # text 안됨
            root = etree.fromstring(data.content)

            # print(root)  # <Element rss at 0x157443c4a80>
            print(root.tag)

            # 서울에 해당하는 location 만 찾기
            items = root.find("channel").find(
                "item").find("description").find("body").find("location")

            for seoul in items.getchildren():
                if seoul.tag == "data":
                    for days in seoul.getchildren():
                        print(days.tag, "=>", days.text)
                        if days.tag == "tmEf":
                            weather_dict["날짜"] = days.text
                        elif days.tag == "wf":
                            weather_dict["날씨"] = days.text
                    weathers.append(weather_dict)
                    weather_dict = {}

            print(weathers)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    parseData()
