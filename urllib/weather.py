import urllib.request as req

# 기상청에서 오늘의 날씨 중 서울.경기도 RSS

weather_url = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109'

data = req.urlopen(weather_url).read()

text = data.decode("utf-8")
# print(text)
print(text[:4000])
