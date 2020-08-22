import requests
from urllib.error import HTTPError
# 기상청에서 오늘의 날씨 중 서울.경기도 RSS

try:

    with requests.Session() as s:
        weather_url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'
        data = s.get(weather_url)
        print(data.text[500:4000])

except HTTPError as e:
    print(e)
