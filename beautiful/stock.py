import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

userAgent = UserAgent()
headers = {
    'user-agent': userAgent.chrome
}

# 웹 페이지 가져오기
res = requests.get('https://finance.naver.com/', headers=headers)

# print(res.content)  # 페이지를 전부 가져오는 건 의미 없음

# 웹 페이지 파싱하기
# 일반적으로 쓰이는 parser 쓰는 것
soup = BeautifulSoup(res.content, 'html.parser')
# print(soup)

# 필요 데이터 추출하기 => table.tbl_home 으로 시작하면 너무 많음


stock5 = soup.select(
    'div.aside_area.aside_popular > table > tbody > tr > th > a')

# 필요 데이터 활용하기
for item in stock5:
    print(item.get_text())

# copy selector
# #container > div.aside > div.group_aside > div.aside_area.aside_popular > table > tbody > tr:nth-child(1) > th > a
