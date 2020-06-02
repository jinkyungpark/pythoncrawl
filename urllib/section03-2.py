# Get 방식 데이터 통신
# 페이로드 : 서버에 정보를 담아서 보내고 결과 받기

import urllib.request
from urllib.parse import urlparse

# ipify : api로 요청을 보내면 응답 해주는 서버
api = "https://api.ipify.org"

# get 방식 파라메터
# values = {
#     'format': 'text'
# }
values = {
    'format': 'json'
}
print('before param : {}'.format(values))
params = urllib.parse.urlencode(values)
print('after param : {}'.format(params))

# 요청 url 생성
url = api+"?"+params
print("요청 URL = {}".format(url))


# 수신 데이터 읽기
data = urllib.request.urlopen(url).read()


# 수신 데이터 디코딩
text = data.decode("utf-8")
print('response : {}'.format(text))
