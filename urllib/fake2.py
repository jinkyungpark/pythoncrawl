from fake_useragent import UserAgent
import urllib.request as request


try:
    # 객체 생성
    userAgent = UserAgent()

    url = "https://news.v.daum.net/v/20200822103818849"

    headers = {
        'User-agent': userAgent.chrome
    }

    request_url = request.Request(url, headers=headers)
    info = request.urlopen(request_url)
    response = info.read().decode("utf-8")
except Exception as e:
    print(e)
else:
    print()
    print("response headers {}".format(info.info()))  # respons headers 정보
    print("request headers {}".format(request_url.header_items()))
