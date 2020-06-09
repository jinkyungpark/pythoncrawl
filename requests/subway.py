# 위키피디아 - 서울 지하철 검색 결과 가져오기
#
import requests
from urllib.error import HTTPError, URLError

# url 한글 문자열 처리
# url = "https://ko.wikipedia.org/wiki/"
# subway_name = "서울_지하철"
# path = parse.quote(subway_name)

# url = url+path

try:
    url = "https://en.wikipedia.org/wiki/Seoul_Metropolitan_Subway"
    with requests.Session() as s:
        res = s.get(url)
except HTTPError as e:
    print('Http Error')
except URLError as e:
    print('URL Error')
else:
    print(res.text)
