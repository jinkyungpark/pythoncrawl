import requests
from bs4 import BeautifulSoup

# 페이지 요청 - 위키피디아 서울지히철

res = requests.get(
    "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0")

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
