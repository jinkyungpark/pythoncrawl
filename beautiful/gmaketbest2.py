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
    print(i, name.get_text(), title.get_text(), price.get_text())


# my
# for i, item in enumerate(items,1):
#     title = item.select_one('a.itemname')
#     price = item.select_one('div.s-price > strong')
#     # a 태그에 들어있는 url 가져오기
#     company_url = item.find("a")
#     # print(company_url.attrs['href'])
#     product_names = requests.get(company_url.attrs['href'])
#     company_res = BeautifulSoup(product_names.content,'html.parser')
#     name = company_res.select_one('div.item-topinfo_headline > p > a > strong')
#     # print(name.string) # get_text()안됨
#     print(i,name.string, title.get_text(),price.get_text())
