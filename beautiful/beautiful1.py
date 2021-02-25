# BeautifulSoup
# 다양한 파서 사용 가능(html.parser, lxml,....)
# 태그, 이름, 속성(아이디, 클래스)로 원하는 요소를 찾을 수 있음
# 


import requests
from bs4 import BeautifulSoup

# 페이지 요청 - 다음 뉴스

res = requests.get(
    "https://news.v.daum.net/v/20210225191120893")

soup = BeautifulSoup(res.text, "html.parser")

# 일반 출력
# print(soup)
# 이쁘게 출력하기
# print(soup.prettify())
print(soup.head)  # <head> ~ </head> 영역에 있는 모든 내용 가져옴
print("\n")
# print(soup.body)  # <body> 태그 안에 있는 내용
print("\n")
print("title ", soup.title)
print("title 태그 이름 ", soup.title.name)
print("title 태그 문자열 ", soup.title.string)
print("title 태그 문자열 ", soup.title.get_text())
