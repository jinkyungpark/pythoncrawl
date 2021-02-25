# beautifulsoup 사용
# 스크랩핑 도구로 유명함
from bs4 import BeautifulSoup  # beautifulsoup4

with open("./beautiful/story.html", "r") as f1:
    html = f1.read()


# Beautifulsoup 단계
# bs4 초기화 - 웹에서 가져온 문서를 첫번째 인자로, 문서의 구조를 두번째 인자로
soup = BeautifulSoup(html, 'html.parser')

# -----------------------------------------------------------------------------

# 타이틀 태그 전체 출력
print("\n---- find()로 정보 찾기")
title = soup.find("title")
print("title >> {}".format(title))
# 타이틀 태그 내용 출력
print("title text >> {}".format(title.string))
# 타이틀 태그의 부모 태그 출력
print("title parent >> {}".format(title.find_parent("head")))  # <head> ~ </head>

# --------------------------------------------------------------------------------
print("\n**** h1 찾기")
h1 = soup.find("h1")
print("h1 >> {}".format(h1))
print("h1 text >>> ", h1.string)

# --------------------------------------------------------------------------------

print("\n**** h2 찾기")
h2 = soup.find("h2")
print("h2 >> {}".format(h2))
print("h2 text >>> ", h2.string)

# --------------------------------------------------------------------------------

# 첫번째 p 태그
print("\n**** p 태그 찾기")
p1 = soup.find("p")
print("p >> {}".format(p1))
print("p text >>> ", p1.string)
# --------------------------------------------------------------------------------

# 첫번째 p 태그
print("\n**** p 태그 찾기2")
p1 = soup.find("p", class_="title")
print("p >> {}".format(p1))
print("p text >>> ", p1.string)

# --------------------------------------------------------------------------------
# 두번째 p 태그
print("\n**** 두번째 p 태그 찾기")
p2 = soup.find("p", class_="story")
print("p >> {}".format(p2))
print("p text >>> ", p2.get_text())

# --------------------------------------------------------------------------------
# 학생들 실습 - 세번째 p 태그 접근
print("\n**** 세번째 p 태그 찾기")
p3 = soup.find("p", class_="story").find_next_sibling()
print(p3.prettify())

# --------------------------------------------------------------------------------
print("\n**** b 태그 찾기")
b = soup.find("b")
print(b.prettify())
# --------------------------------------------------------------------------------
# a 태그 찾기
print("\n**** 첫번째 a 태그 찾기")
a1 = soup.find("a")
print(a1.prettify())

# --------------------------------------------------------------------------------
# a 태그 찾기
print("\n**** 두번째 a 태그 찾기")
a2 = soup.find("a", id="link2")
print("a : {}".format(a2))
print("a text : {}".format(a2.string))

# --------------------------------------------------------------------------------
# a 태그 찾기
print("\n**** 세번째 a 태그 찾기")
a3 = soup.find("a", {"class": "sister", "data-io": "link3"})
print("a : {}".format(a3))
print("a href : {}".format(a3['href']))
print("a text : {}".format(a3.string))

# --------------------------------------------------------------------------------

# 함수확인 - p2에서 사용가능한 함수들
print(dir(p2))

# --------------------------------------------------------------------------------

# 반복 출력 확인 - p2의 다음 요소인 텍스트 엘리먼트 출력
print()
for v in p2.next_element:
    print(v, end='')  # end를 안 주면 글자 한자씩 나옴
