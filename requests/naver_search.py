import requests
from urllib.error import URLError


search_url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8"

param = {"query": "영화"}

try:
    with requests.Session() as s:
        response = s.get(search_url, params=param)
        # 앞 쪽의 데이터는 스크립트라서
        print(response.text[130000:150000])
except URLError as e:
    print("URLError")
