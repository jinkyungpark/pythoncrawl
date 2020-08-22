import requests
from urllib.error import HTTPError

# 행정 안전부 : https://www.mois.go.kr

# 가져올 rss 주소
url = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'

# 뒤에 붙는 파라메터 코드값에 의해 가져오는 정보가 달라지므로 동적으로 처리
params = []

try:
    for num in [1001, 1012, 1013, 1014]:
        params.append(dict(ctxCd=num))

    # 중간 확인
    print(params)

    with requests.Session() as r:

        # 연속해서 4번 요청
        for param in params:
            # 요청
            res_data = requests.get(url, params=param)
            # 출력하기
            print("-"*100)
            print(res_data.text)
except HTTPError as e:
    print(e)
