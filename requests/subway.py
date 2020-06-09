# 위키피디아 - 서울 지하철 검색 결과 가져오기
#

import urllib.request as req
import urllib.parse as parse
from urllib.error import HTTPError

# url 한글 문자열 처리
# url = "https://ko.wikipedia.org/wiki/"
# subway_name = "서울_지하철"
# path = parse.quote(subway_name)

# url = url+path

try:
    url = "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0"
    res = req.urlopen(url).read().decode("utf-8")
except HTTPError as e:
    print('Http Error')
else:
    print(res)

# 한글로 된 경로명들이 모두 인코딩 되서 넘어오기 때문에 unquote를 한번 씀
# print(parse.unquote(res.decode("utf-8")))
