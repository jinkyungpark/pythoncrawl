# 공공 API 시도별 실시간 평균정보 조회
# https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000581
import requests

"""
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : '서비스키', quote_plus('numOfRows') : '10', quote_plus('pageNo') : '1', 
quote_plus('itemCode') : 'PM10', quote_plus('dataGubun') : 'HOUR', quote_plus('searchCondition') : 'MONTH' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body
"""

url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureLIst?'
service_key = 'onr2dF6kAgGjBXVxNMOm2DSD6wsM24sEsylFqWITUO0x5S%2FkGMBhTHF36x1rwpkWaowKB6oM0jrArcmquppyyg%3D%3D'
numOfRows = '10'
pageNo = '1'
itemCode = 'PM10'
dataGubun = 'HOUR'
searchCondition = 'MONTH'

request_url = url+'serviceKey='+service_key+"&numOfRows="+numOfRows+"&pageNo="+pageNo + \
    "&itemCode="+itemCode+"&dataGubun="+dataGubun+"&searchCondition="+searchCondition

res = requests.get(request_url)
print(res.text)  # xml로 오는 데이터
