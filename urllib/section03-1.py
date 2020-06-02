# Get 방식 데이터 통신
import urllib.request
from urllib.parse import urlparse

# 엔카 : 기본요청
url = "http://www.encar.com"

# 수신된 정보 변수에 담기
mem = urllib.request.urlopen(url)

# 수신된 정보 출력
print('type : {}'.format(type(mem)))  # <class 'http.client.HTTPResponse'>
print('geturl : {}'.format(mem.geturl()))  # http://www.encar.com/index.do
print('status : {}'.format(mem.status))  # 200
print('header : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))  # 200
# 읽어올 바이트 수 : 100(너무 크면 에러 남)
print('read : {}'.format(mem.read(100).decode('utf-8')))
# 전체 정보
print('parse : {}'.format(urlparse('http://www.encar.co.kr?test=test')))
# 전체 정보 중에서 query만
print('parse : {}'.format(urlparse('http://www.encar.co.kr?test=test').query))

# 페이로드 : 서버에 정보를 담아서 보내고 결과 받기
