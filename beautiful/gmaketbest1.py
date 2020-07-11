import requests
from bs4 import BeautifulSoup
# divided and conquer : 분할하고 정복

# 크롤링 데이터를 다시 크롤링
# g마켓 => BEST => 컴퓨터/전자 크롤링

# 경로 
url = 'http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G06'

res = requests.get(url)

soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)

# 처음에 이렇게 뽑았을 때 문제점이 best-list 라는 클래스명을 가진 영역이 두개 있었음(100개가 넘게 뽑힐수도)
# for i, item in enumerate(lis_items,1):
#     titles = item.select('li > a')
#     prices = item.select('div.s-price > strong > span > span')
#     for title in titles:
#         print(i, title.get_text(),end='   ') 
#     for price in prices:   
#         print(price.get_text())

# teacher 방식
lis = soup.select('div.best-list')
lis_items = lis[1]
# print(lis_items)   

items = lis_items.select('ul > li')
for i, item in enumerate(items,1):
    title = item.select_one('a.itemname')
    price = item.select_one('div.s-price > strong')
    print(i, title.get_text(),price.get_text()) 
    
