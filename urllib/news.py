# 학생들 실습 - 다음 뉴스 기사 가져오기
from urllib.request import urlopen
from urllib.error import HTTPError


url = "https://news.v.daum.net/v/20200822103818849"


try:
    response = urlopen(url).read().decode("utf-8")
except HTTPError as e1:  # 주소 잘못된 경우
    print(e1)
else:
    print(response)
