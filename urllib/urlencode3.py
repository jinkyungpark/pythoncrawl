import urllib.request as req
from urllib.parse import urlencode
from urllib.error import URLError

# 네이버 검색 창에서 영화라는 검색어를 넣고 검색하는 경우
# search_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%98%81%ED%99%94"

search_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&"

param = {"query": "영화"}

param = urlencode(param)

search_url = search_url + param

try:
    data = req.urlopen(search_url).read().decode("utf-8")
except URLError as e:
    print("URLError")
else:
    # 앞 쪽의 데이터는 스크립트라서
    print(data[150000:200000])  # 150000 ~ 200000
