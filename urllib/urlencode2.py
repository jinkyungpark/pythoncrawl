# Get 방식 데이터 통신
# 페이로드 : 서버에 정보를 담아서 보내고 결과 받기

from urllib.request import urlopen
from urllib.parse import urlparse, urlencode

# ipify : api로 요청을 보내면 응답 해주는 서버
api = "https://api.ipify.org"

# get 방식 파라메터
# values = {
#     'format': 'text'
# }

# json 형식의 데이터를 그냥 보내는 경우
values = {"format": "json"}
# url = api + "?" + values
# print("before param : {}".format(values))
# print("요청 URL = {}".format(url))

# ---------------------- 여기까지 하고 실행하면 에러남


# url로 쿼리문 전송시 인코딩
params = urlencode(values)
print("after param : {}".format(params))

# 요청 url 생성
url = api + "?" + params
print("요청 URL = {}".format(url))


# 수신 데이터 읽기
data = urlopen(url).read()


# 수신 데이터 디코딩
text = data.decode("utf-8")
print("response : {}".format(text))

