import requests
import json

# 컴퓨터 / 식품
try:
    url_list = [
        'https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=B02&durationDays=30&count=100&_=1593610979071',
        'https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=D01&durationDays=30&count=100&_=1593610880660'
    ]

    with requests.Session() as s:
        for url in url_list:
            res = s.get(url)

            top100 = json.loads(res.text)

            # print('확인 : ', top100)
            print(url)
            for i, item in enumerate(top100, 1):
                if i < 101:  # 163개까지 가져와서 이렇게 처리함
                    print(i, item['product_name'])
            print()
except Exception as e:
    print(e)
