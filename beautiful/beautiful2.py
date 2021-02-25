import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# 웹 페이지 가져오기
userAgent = UserAgent()
headers = {
    'user-agent': userAgent.chrome
}
res = requests.get(
    'https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=100&oid=001&aid=0011714558', headers=headers)
# print(res.text)  # 페이지를 전부 가져오는 건 의미 없음

# 웹 페이지 파싱하기
# 일반적으로 쓰이는 parser 쓰는 것
soup = BeautifulSoup(res.content, 'html.parser')
print(type(soup))
# print(soup)

# 필요 데이터 추출하기
title = soup.find('h3', id='articleTitle')

# 필요 데이터 활용하기
print(title.get_text())
# print(title.string)


# Beautifulsoup 단계
# bs4 초기화 - 웹에서 가져온 문서를 첫번째 인자로, 문서의 구조를 두번째 인자로
