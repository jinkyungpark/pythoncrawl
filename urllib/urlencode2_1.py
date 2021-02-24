# Get 방식 데이터 통신
# 페이로드 : 서버에 정보를 담아서 보내고 결과 받기

from urllib.request import urlopen
from urllib.parse import urlencode

# ipify : api로 요청을 보내면 응답 해주는 서버
api = "https://api.ipify.org"

# get 방식 파라메터
values = {
    'format': 'text'
}
# json 형식의 데이터를 그냥 보내는 경우
# values = {"format": "json"}

url = api + "?" + urlencode(values)
print("before param : {}".format(values))
print("요청 URL = {}".format(url))
print("after param : {}".format(urlencode(values)))

# 수신 데이터 읽기
data = urlopen(url).read().decode("utf-8")
print("response : {}".format(data))

