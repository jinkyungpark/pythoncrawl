import json
import requests
import pprint  # json 을 이쁘게 출력하기

client_id = '6_FpNFqYVz7PeiPV7Omd'
client_secret = 'S7f9ozjfRZ'

naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=android'

header_params = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

res = requests.get(naver_open_api, headers=header_params)

if res.status_code == 200:
    # json 형태로 출력
    # data = res.json()   # json.loads()와 비슷한 역할
    # print(data)
    # print()
    # print(data['items'][0])  # 첫번째 상품만 출력
    # print(data['items'][0]['title'])  # 파인디지털 파인드라이브 Q30

    # print()
    # pprint.pprint(data['items'])  # json 이쁘게 출력하기

    # 현재 출력된 상품들의 타이틀과 링크만 출력하기
    for index, item in enumerate(data['items'], 1):
        print(index, item['title'], item['link'])

else:
    print("Error code : ", res.status_code)
