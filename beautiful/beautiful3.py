# beautifulsoup 사용
# 스크랩핑 도구로 유명함
from bs4 import BeautifulSoup  # beautifulsoup4

with open("./beautiful/story.html", "r") as f1:
    html = f1.read()


# Beautifulsoup 단계
# bs4 초기화 - 웹에서 가져온 문서를 첫번째 인자로, 문서의 구조를 두번째 인자로
soup = BeautifulSoup(html, 'html.parser')

# 타입확인
print('soup', type(soup))  # soup <class 'bs4.BeautifulSoup'>
# print(soup.prettify())

# -----------------------------------------------------------------------------


# 타이틀 태그 전체 출력
print("title >> {}".format(soup.title))
# 타이틀 태그 내용 출력
print("title text >> {}".format(soup.title.string))
# 타이틀 태그의 부모 태그 출력
print("title parent >> {}".format(soup.title.parent))  # <head> ~ </head>


# --------------------------------------------------------------------------------

# find 를 사용하는 경우
print("\nfind() 사용")
print("title >> {}".format(soup.find("title")))
print("title text >> {}".format(soup.find("title").string))

# --------------------------------------------------------------------------------

# h1 태그 접근
print()
# h1 = soup.html.body.h1
h1 = soup.body.h1
print("h1 >>", h1)

# 첫번째 p 태그 접근
print()
# p1 = soup.html.body.p
p1 = soup.p
print("p1 >>> ", p1)
# 첫번째 p가 가지고 있는 클래스명 구하기
print("p1 class >>> ", p1['class'])

# --------------------------------------------------------------------------------

# find 를 사용하는 경우
print("\nfind() 사용")
print("title >> {}".format(soup.find("h1")))
p1 = soup.find("p")
print("p1 class >>> ", p1['class'])


# --------------------------------------------------------------------------------


# 두번째 p 태그 접근
# next_sibling : p 태그 다음의 공백 의미
print()
p2 = p1.next_sibling.next_sibling
print(p2.prettify())


# --------------------------------------------------------------------------------

# 두번째 p 태그 접근 - find_next_sibling()
# next_sibling : p 태그 다음의 공백 의미
print("\n--next_sibling()--")
p2 = p1.find_next_sibling()
print(p2.prettify())

# --------------------------------------------------------------------------------

# 학생들 실습 - 세번째 p 태그 접근
print()
p1 = soup.find("p")
p2 = p1.next_sibling.next_sibling
p3 = p2.next_sibling.next_sibling
print(p3.prettify())

# --------------------------------------------------------------------------------
print("\n--find_next_sibling() 두 번")
p3 = soup.find("p").find_next_sibling().find_next_sibling()
print(p3.prettify())

# --------------------------------------------------------------------------------
# 가져온 태그가 가지고 있는 텍스트 출력
print()
print("h1 >>", h1.string)
print("p1 >>", p1.string)
print("p2 >>", p2.string)
print("p3 >>", p3.string)


# 함수확인 - p2에서 사용가능한 함수들
print(dir(p2))


# 반복 출력 확인 - p2의 다음 요소인 텍스트 엘리먼트 출력
print()
for v in p2.next_element:
    print(v, end='')  # end를 안 주면 글자 한자씩 나옴
