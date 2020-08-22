# requests 사용 스크랩핑


import requests
import json

# post 방식으로 요청 / timeout 부여
with requests.Session() as s:
    param = {"test": "name"}
    # 요청
    r = s.get('https://httpbin.org/get', params=param)

    print(r.headers)
    # 출력
    print(r.text)
