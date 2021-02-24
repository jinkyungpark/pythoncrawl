import urllib.request as req
from urllib.error import HTTPError


try:
    url = "http://www.11st.co.kr/browsing/BestSeller.tmall?method=getBestSellerMain&genderType=F"
    # 11번가는 charset=EUC-KR 이라서 utf-8로 주변 에러남
    response = req.urlopen(url)
    contents = response.read().decode("euc-kr")

except HTTPError as e:
    print(e)
else:
    print("heder Info - {}".format(response.info()))
    print("content {}".format(contents[:3000]))
