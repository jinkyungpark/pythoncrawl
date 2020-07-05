import requests
import json

client_id = '6_FpNFqYVz7PeiPV7Omd'
client_secret = 'S7f9ozjfRZ'

# query : 검색을 원하는 문자열
# display : 검색결과 출력건수 지정(기본:10, 최대 : 100)
# start : 검색 시작 위치로 최대 1000까지 가능(기본 1, 최대 : 1000)
# sort : 정렬옵션

# 주소 만들기 + 정보 가져오기
# https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start=1

header_params = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

start, num = 1, 0
for idx in range(10):
    start_num = start + (idx*100)

    naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start=' + \
        str(start_num)
    # print(naver_open_api)

    res = requests.get(naver_open_api, headers=header_params)

    data = res.json()

    if res.status_code == 200:
        for item in data['items']:
            num += 1
            print(num, item['title'], item['link'])
    else:
        print("Error code : ", res.status_code)
