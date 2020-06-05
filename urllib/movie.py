import urllib.request as req
from urllib.error import HTTPError, URLError

# 영화진흥위원회 어제 날짜의 박스오피스 데이터를 가져와서
# 파일로 저장하기
movie_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.xml?key=430156241533f1d058c603178cc3ca0e&targetDt=20200604"

try:
    data = req.urlopen(movie_url).read().decode("utf-8")
except HTTPError as e:
    print('Http Error')
except URLError as e:
    print('URL Error')
else:
    print()
    with open('c:/data/movie.txt', 'w') as c:
        c.write(data)
