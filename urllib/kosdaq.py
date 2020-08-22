# Get 방식 데이터 통신
# 다음 주식 정보 가져오기
# fake-useragent 사용
# header 삽입

import json   # 넘어오는 데이터가 json 이기 때문에
import urllib.request as req
import csv
from fake_useragent import UserAgent

userAgent = UserAgent()
# print(userAgent.ie)
# print(userAgent.msie)
# print(userAgent.chrome)
# print(userAgent.safari)
# print(userAgent.random)

# 헤더 정보
headers = {
    'User-agent': userAgent.ie,
    'referer': 'http://finance.daum.net/'
}

# 다음 주식 요청 URL
url = 'http://finance.daum.net/api/search/ranks?limit=10'

# 요청하기
# 헤더 값을 같이 보내려면 Request 객체 필요
res = req.urlopen(req.Request(url, headers=headers)).read().decode("UTF-8")

# 정보 가져오기
# print(res) - 이쁘게 만들기 전
rank_json = json.loads(res)['data']

# 중간확인
# print('중간확인 : ',rank_json,'\n')


data = []
# 반복문을 돌려 출력하기
for element in rank_json:
    # 화면 출력
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(
        element['rank'], element['name'], element['tradePrice']))
    data.append(element)

    # 파일(CSV, 엑셀, txt) 저장 및 db 저장
    with open("c:/download/finance.txt", "a") as txt,  open("c:/download/finance.csv", "w", newline="") as csvfile:  # 인코딩을 넣으면 한글 깨짐
        # 파일 저장
        txt.write('순위 : {}, 금액 : {}, 회사명 : {}\n'.format(
            element['rank'], element['name'], element['tradePrice']))

        # csv 저장
        output = csv.writer(csvfile)
        output.writerow(data[0].keys())  # header row
        for row in data:
            output.writerow(row.values())  # value
