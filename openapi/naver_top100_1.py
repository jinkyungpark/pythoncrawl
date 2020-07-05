import requests

client_id = '6_FpNFqYVz7PeiPV7Omd'
client_secret = 'S7f9ozjfRZ'

# query : 검색을 원하는 문자열
# display : 검색결과 출력건수 지정(기본:10, 최대 : 100)
# start : 검색 시작 위치로 최대 1000까지 가능(기본 1, 최대 : 1000)
# sort : 정렬옵션

# 주소 만들기(sort는 안주면  유사도순이 기본갑)
# https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start=1

header_params = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}


start = 1
for idx in range(10):
    start_num = start + (idx*100)

    naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start=' + \
        str(start_num)
    print(naver_open_api)
