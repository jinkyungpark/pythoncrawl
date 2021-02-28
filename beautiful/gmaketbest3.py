# divided and conquer : 분할하고 정복
import requests
from bs4 import BeautifulSoup
import openpyxl

# 엑셀 파일 저장 준비
gmarket_best100 = openpyxl.Workbook()

sheet = gmarket_best100.active
sheet.title = '베스트100'
sheet.column_dimensions['B'].width = 30
sheet.column_dimensions['C'].width = 80
sheet.column_dimensions['D'].width = 75
sheet.column_dimensions['E'].width = 20
sheet.append(['번호', '회사명', '제품명', '상세정보 url', '가격'])
##################################


# 크롤링 데이터를 다시 크롤링
# g마켓 => BEST => 컴퓨터/전자 크롤링

# 경로
url = 'http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06'

res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)

lis = soup.select('div.best-list')
lis_items = lis[1]
# print(lis_items)

items = lis_items.select('ul > li')
for i, item in enumerate(items, 1):
    title = item.select_one('a.itemname')
    price = item.select_one('div.s-price > strong')
    # a 태그에 들어있는 url 가져오기
    # print(title['href'])
    product_url = requests.get(title['href'])
    company_res = BeautifulSoup(product_url.content, 'html.parser')
    name = company_res.select_one(
        'div.item-topinfo > div.item-topinfo_headline > p > span > a')
    # print(name.get_text())
    # print(i,name.get_text(), title.get_text(),price.get_text())

    # 엑셀파일로 저장하기
    sheet.append([i, name.get_text(), title.get_text(),
                  title['href'], price.get_text()])

    # 주소가 들어 있는 부분 하이퍼링크 걸어주기
    sheet.cell(row=i+1, column=4).hyperlink = title['href']

# 셀 선택하기
cell_A1 = sheet['A1']
# 중앙정렬
cell_A1.alignment = openpyxl.styles.Alignment(horizontal='center')
# 글자 색상 변경
cell_A1.font = openpyxl.styles.Font(color="01579B")

# 셀 선택하기
cell_B1 = sheet['B1']
# 중앙정렬
cell_B1.alignment = openpyxl.styles.Alignment(horizontal='center')
# 글자 색상 변경
cell_B1.font = openpyxl.styles.Font(color="01579B")

# 셀 선택하기
cell_C1 = sheet['C1']
# 중앙정렬
cell_C1.alignment = openpyxl.styles.Alignment(horizontal='center')
# 글자 색상 변경
cell_C1.font = openpyxl.styles.Font(color="01579B")

# 셀 선택하기
cell_D1 = sheet['D1']
# 중앙정렬
cell_D1.alignment = openpyxl.styles.Alignment(horizontal='center')
# 글자 색상 변경
cell_D1.font = openpyxl.styles.Font(color="01579B")


# 셀 선택하기
cell_E1 = sheet['E1']
# 중앙정렬
cell_E1.alignment = openpyxl.styles.Alignment(horizontal='center')
# 글자 색상 변경
cell_E1.font = openpyxl.styles.Font(color="01579B")

gmarket_best100.save('c:\\gmarket_best100.xlsx')
gmarket_best100.close()
