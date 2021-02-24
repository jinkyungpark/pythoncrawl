import urllib.request as request
from urllib.error import URLError

# 네이버 뉴스 기사의 경우에 그냥 크롤링을 돌리면
# http.client.RemoteDisconnected: Remote end closed connection without response
# url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=032&aid=0003061030"
url = "https://news.v.daum.net/v/20210224220416972"
try:
    # 이 코드가 먼저 와야 함
    request_url = request.Request(url)
    res = request.urlopen(request_url).read().decode("utf-8")
except URLError as e:
    print(e)
else:
    print(res[:2000])
    print(request_url.header_items())
