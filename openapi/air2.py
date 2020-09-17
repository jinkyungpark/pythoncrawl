# 공공 API 시도별 실시간 평균정보 조회
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000581
import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'
param = {
    "serviceKey": unquote('onr2dF6kAgGjBXVxNMOm2DSD6wsM24sEsylFqWITUO0x5S%2FkGMBhTHF36x1rwpkWaowKB6oM0jrArcmquppyyg%3D%3D'),
    "numOfRows": '10',
    "pageNo": '1',
    "itemCode": 'PM10',
    "dataGubun": 'HOUR',
    "searchCondition": 'MONTH'
}

res = requests.get(url, params=param)
# print(res.text)  # xml로 오는 데이터

# 파싱하기
soup = BeautifulSoup(res.content, 'html.parser')

# 원하는 값 추출하기 : find, find_all() / select 불가(css 없기 때문에)
# 서울 지역의 시간대별 PM10 지수 추출

data = soup.find_all('item')
for item in data:
    print(item)
    datatime = item.find('datatime')
    seoul = item.find('seoul')
    print('%s PM10 지수 : %s' % (datatime.get_text(), seoul.get_text()))
