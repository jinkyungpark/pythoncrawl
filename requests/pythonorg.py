import requests
from urllib.error import HTTPError, URLError

# try:
#     url = "https://www.python.org/"
#     with requests.Session() as s:
#         res = s.get(url)
# except HTTPError as e:
#     print('Http Error')
# except URLError as e:
#     print('URL Error')
# else:
#     print(res.text)


# 앞의 서울지하철 정보와 python.org 를 한꺼번에 처리하면
url_list = ['https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway',
            'https://www.python.org/']
with requests.Session() as s:
    for url in url_list:
        res = s.get(url)
        print(res.text[:500])
        print()
