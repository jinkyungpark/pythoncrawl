import requests
import json
import openpyxl

client_id = '6_FpNFqYVz7PeiPV7Omd'
client_secret = 'S7f9ozjfRZ'

# 주소 + 요청 + 엑셀저장
header_params = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

# 엑셀저장
excel_file = openpyxl.Workbook()

excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 100
excel_sheet.column_dimensions['C'].width = 60
excel_sheet.append(['순위', '상품명', '주소'])  # 타이틀 행 지정
excel_sheet.title = '샤오미 top1000'  # 시트 이름 지정

start, num = 1, 0

for idx in range(10):
    start_num = start + (idx*100)

    naver_open_api = 'https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start=' + \
        str(start_num)
    # print(naver_open_api)

    res = requests.get(naver_open_api, headers=header_params)

    data = res.json()

    if res.status_code == 200:
        for item in data['items']:
            num += 1
            product_info = [num, item['title'], item['link']]
            excel_sheet.append(product_info)
    else:
        print("Error code : ", res.status_code)

excel_file.save('c:/샤오미.xlsx')
excel_file.close()
