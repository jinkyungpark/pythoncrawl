# Get 방식 데이터 통신
# 페이로드 : 서버에 정보를 담아서 보내고 결과 받기

from urllib.request import urlopen

# ipify : api로 요청을 보내면 응답 해주는 서버
# 파라메터를 딸려 보낼때 아래처럼 작업하면 되긴 되지만
# 텍스트 형태로 받기 위해서는 또 변경이 필요한 상황임
api = "https://api.ipify.org"

values = {"format": "text"}

url = api + "?" + values
print("요청 URL = {}".format(url))

response = urlopen(url).read().decode("utf-8")
print(response)
