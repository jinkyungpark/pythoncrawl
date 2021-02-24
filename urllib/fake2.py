from fake_useragent import UserAgent
import urllib.request as request


try:
    # 객체 생성
    userAgent = UserAgent()

    # 네이버 뉴스의 경우에는 필히 userAgent 사용해야 함
    # url = "https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=032&aid=0003061030"

    url = "https://news.v.daum.net/v/20200822103818849"

    headers = {
        'User-agent': userAgent.chrome
    }

    # header 정보를 딸려 보내기 위해서는 Request 클래스를 사용해서 정보를 보낸다
    request_url = request.Request(url, headers=headers)
    info = request.urlopen(request_url)

    # 네이버 뉴스 기사는 euc-kr 로 해야 됨
    # 'utf-8' codec can't decode byte 0xbf in position 223: invalid start byte
    response = info.read().decode("utf-8")
except Exception as e:
    print(e)
else:
    print()
    print("response headers {}".format(info.info()))  # respons headers 정보
    print("request headers {}".format(request_url.header_items()))
