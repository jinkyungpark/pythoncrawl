import requests
import json

res = requests.get(
    'https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1593607390137')

# requests.get()으로 가져온 데이터의 내용을 출력하기 위해서는 res.content 반드시 필요
top100 = json.loads(res.content)

# print('확인 : ', top100)

for i, item in enumerate(top100, 1):
    if i < 101:  # 163개까지 가져와서 이렇게 처리함
        print(i, item['product_name'])
