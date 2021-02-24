import urllib.request as req
from urllib.error import HTTPError, URLError

# 영화진흥위원회 어제 날짜의 박스오피스 데이터를 가져와서
# 파일로 저장하기
movie_url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=f5eef3421c602c6cb7ea224104795888&targetDt=20200222"

try:
    data = req.urlopen(movie_url).read().decode("utf-8")
except HTTPError as e:
    print('Http Error')
except URLError as e:
    print('URL Error')
else:
    print()
    with open('c:/download/movie.txt', 'w') as c:
        c.write(data)
