# requests 사용 스크랩핑
# 수신 데이터를 json 변환 출력

import requests
import json

# 세션 활성화 및 json 데이터 요청
# with requests.Session() as s:
#     r = s.get('https://httpbin.org/stream/10', stream=True)  # stream 을 주면 좋다
#     print(r.text)   # 기본 형태로 출력


# 세션 활성화 및 json 데이터 요청 / 인코딩 확인 후 set하기
# with requests.Session() as s:
#     r = s.get('https://httpbin.org/stream/10', stream=True)   # stream + True 는 Raw Response Content 인경우 사용하라고 되어 있음
#     print("encoding:{}".format(r.encoding))   # encoding 이 None 임
#     if r.encoding is None:
#         r.encoding = 'UTF-8'
#         print("encoding:{}".format(r.encoding))


# 세션 활성화 및 json 데이터 요청 / 인코딩 확인 후 set하기
with requests.Session() as s:
    r = s.get('https://httpbin.org/stream/10', stream=True)
    print("Headers {} ".format(r.headers))
    # print(r.json()) 에러남(json 형태이긴 하나 parse인 못한다고 되어 있음 사이트에서 제공하지 못함)

    if r.encoding is None:
        r.encoding = 'UTF-8'

    # json 변환 출력
    for line in r.iter_lines(decode_unicode=True):
        # 라인 출력 후 타입 확인
        print(line)
        print(type(line))  # <class 'str'>

        # json => 딕셔너리 변환
        # b = json.loads(line)  # str -> 딕셔너리 변환
        # print(type(b))   # <class 'dict'>

        # for k, v in b.items():
        #     print("Key : {}, Value : {}".format(k, v))
        # print()
        # print()
