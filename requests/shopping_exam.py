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

            for i, item in enumerate(res.json(), 1):
                if i < 101:
                    print(i, item["product_name"])
            print("*" * 30)
            
except Exception as e:
    print(e)
