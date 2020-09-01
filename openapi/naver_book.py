import requests
from bs4 import BeautifulSoup
import pprint
import openpyxl


# 엑셀 파일
excel_file = openpyxl.Workbook()

excel_sheet = excel_file.active
excel_sheet.column_dimensions['B'].width = 30  # isbn
excel_sheet.column_dimensions['C'].width = 100  # title
excel_sheet.column_dimensions['D'].width = 15  # price
excel_sheet.column_dimensions['E'].width = 15  # discount
excel_sheet.append(['번호', 'isbn', '제목', '가격', '할인가격'])
excel_sheet.title = "베르나르 베르베르"


client_id = '6_FpNFqYVz7PeiPV7Omd'
client_secret = 'S7f9ozjfRZ'

naver_open_api = 'https://openapi.naver.com/v1/search/book.json'

headers = {
    "X-Naver-Client-Id": client_id,
    "X-Naver-Client-Secret": client_secret
}

start, num = 1, 1
for idx in range(3):
    start_num = start + (idx*100)
    param = {
        'query': '베르나르 베르베르',
        'display': '100',
        'start': start_num
    }
    res = requests.get(naver_open_api, params=param, headers=headers)

    data = res.json()
    # pprint.pprint(data)

    for item in data['items']:

        print(num, item['isbn'], item['title'],
              item['price'], item['discount'])
        product_info = [num, item['isbn'], item['title'],
                        item['price'], item['discount']]
        excel_sheet.append(product_info)
        num += 1


excel_file.save('c:/베르나르.xlsx')
excel_file.close()
