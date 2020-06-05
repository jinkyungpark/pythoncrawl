# Get 방식 데이터 통신
# 페이로드 : 주소창에 실어서 보내는 것
# 행정안전부 사이트 RSS 데이터 수신
# RSS 란? 새로운 소식이 업데이트가 되어 있는지 알 수 있도록 해주는 것(피드)

import urllib.request
from urllib.parse import urlparse

# 행정 안전부 : https://www.mois.go.kr

# 가져올 rss 주소
api = 'https://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp'

# 뒤에 붙는 파라메터 코드값에 의해 가져오는 정보가 달라지므로 동적으로 처리
params = []

for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))

# 중간 확인
print(params)

# 연속해서 4번 요청
for c in params:
    # 파라메터로 붙는 부분에 대해 인코딩 처리
    param = urllib.parse.urlencode(c)

    # url 완성
    url = api + "?" + param

    # url 확인
    print("url : {}".format(url))

    # 요청
    res_data = urllib.request.urlopen(url).read()

    # 수신 후 디코딩
    contents = res_data.decode('utf-8')

    # 출력하기
    print("-"*100)
    print(contents)
