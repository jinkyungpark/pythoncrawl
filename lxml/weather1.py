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
            items = root.xpath(
                "//channel/item/description/body/location")

            print(items[0])
            for item in items[0]:
                print(item.tag, ":", item.text)
                for days in item:  # item == data
                    print(days.tag, "=>", days.text)

                    # weather_dict[days.tag] = days.text
                    if days.tag == "tmEf":
                        weather_dict["날짜"] = days.text
                    elif days.tag == "wf":
                        weather_dict["날씨"] = days.text
                if weather_dict:  # 위에서 province 태그와 city 태그 때문에 빈 딕셔너리가 앞에 생성됨
                    weathers.append(weather_dict)
                weather_dict = {}

            print(weathers)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    parseData()
