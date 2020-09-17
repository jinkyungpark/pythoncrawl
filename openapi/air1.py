# 공공 API 시도별 실시간 평균정보 조회
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000581
import requests
from urllib.parse import unquote

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
print(res.text)  # xml로 오는 데이터
