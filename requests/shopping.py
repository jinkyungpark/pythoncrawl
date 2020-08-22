import requests
import json
from urllib.error import HTTPError


try:
    with requests.Session as s:
        res = s.get(
            'https://shoppinghow.kakao.com/siso/p/api/bestRank/dispprodbest?vCateId=GMP&durationDays=30&count=100&_=1593607390137')
        top100 = json.loads(res.text)
        # top100 = res.text  # list 형태로 가져옴
        # print(top100)   # list[{},{}] 형태임
        # print(type(top100))

        for i, item in enumerate(top100, start=1):
            if i < 101:  # 164 개까지 가져와서 이렇게 처리함
                print(i, item['product_name'])

except HTTPError as e:
    print(e)


