# requests 사용 스크랩핑
# 수신 데이터를 json 변환 출력
# https://jsonplaceholder.typicode.com/ 사용

import requests
import json

# 세션 활성화 및 json 데이터 요청 / 인코딩 확인 후 set하기
with requests.Session() as s:
    r = s.get('https://jsonplaceholder.typicode.com/users', stream=True)
    # print(r.json())   # 가져온 json 출력

    for line in r.json():
        for k, v in line.items():
            print("Key : {}, Value : {}".format(k, v))
        print()
