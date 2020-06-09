# 위키피디아 - 서울 지하철 검색 결과 가져오기
#

import urllib.request as req
import requests
from lxml.html import fromstring, tostring


url = "https://ko.wikipedia.org/wiki/"
subway_name = "서울_지하철"

res = requests.get(url+subway_name)  # res에는 응답코드만 들어감

data = fromstring(res.content)  # 문자열 저장

# 저장된 문자열에서 원하는 태그 찾기
for a in data.xpath('//*[@id="mw-content-text"]/div/table[1]/tbody/tr[1]/td/a/img'):
    print(tostring(a, pretty_print=True))
