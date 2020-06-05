# requests 사용 스크랩핑
# 수신 데이터를 json 변환 출력
# https://jsonplaceholder.typicode.com/ 사용

import requests
import json

# 세션 활성화 및 json 데이터 요청 / 인코딩 확인 후 set하기
with requests.Session() as s:
    r = s.get('https://jsonplaceholder.typicode.com/todos/1')
    print("headers : {}".format(r.headers))  # 헤더 정보 출력
    print("json : {}".format(r.json()))   # 가져온 json 출력 : 단일 레코드일 때 이렇게 가져옴
    print("r.json().keys() : {}".format(r.json().keys()))  # 키 정보 출력
    print("r.json().values() : {}".format(r.json().values()))  # 값 정보 출력
    print("r.encoding : {}".format(r.encoding))  # 인코딩 확인
    print("r.content :{}".format(r.content))   # binary 형식으로 보여짐
    # b'{\n  "userId": 1,\n  "id": 1,\n  "title": "delectus aut autem",\n  "completed": false\n}'
