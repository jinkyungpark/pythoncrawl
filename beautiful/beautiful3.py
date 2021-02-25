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
# 태그명으로 정보 찾기

print("\n---- 태그로 정보 찾기")
print("title >> {}".format(soup.title))
# 타이틀 태그 내용 출력
print("title text >> {}".format(soup.title.string))
# 타이틀 태그의 부모 태그 출력
print("title parent >> {}".format(soup.title.parent))  # <head> ~ </head>

# --------------------------------------------------------------------------------
print("\n---- h1 태그 찾기")
print("h1 >> {}".format(soup.h1))
print("h1 text >> {}".format(soup.h1.string))

# --------------------------------------------------------------------------------
print("\n---- h2 태그 찾기")
print("h2 >> {}".format(soup.h2))
print("h2 text >> {}".format(soup.h2.string))

# --------------------------------------------------------------------------------
print("\n---- p 태그 찾기")
p1 = soup.p
print("p >> {}".format(p1))
print("p text >> {}".format(p1.string))
print("p class >> {}".format(p1['class']))

# --------------------------------------------------------------------------------
print("\n---- 두번째 p 태그 찾기")
p2 = p1.find_next_sibling("p")
print("p >> {}".format(p2))
print("p text >> {}".format(p2.get_text()))  # string 으로는 안나옴
print("p class >> {}".format(p2['class']))

# --------------------------------------------------------------------------------
print("\n---- 세번째 p 태그 찾기")
# p3 = p2.next_sibling.next_sibling
p3 = p2.find_next_sibling("p")
print("p >> {}".format(p3))
print("p text >> {}".format(p3.get_text()))
print("p class >> {}".format(p3['class']))

# --------------------------------------------------------------------------------
print("\n---- b 태그 찾기")
b = soup.b
print("b >> {}".format(b))
print("b text >> {}".format(b.string))

# --------------------------------------------------------------------------------
print("\n---- a 태그 찾기")
a1 = soup.a
print("a1 >> {}".format(a1))
print("a1 text >> {}".format(a1.string))

# --------------------------------------------------------------------------------
print("\n---- 두 번째 a 태그 찾기")
a2 = a1.find_next_sibling("a")
print("a2 >> {}".format(a2))
print("a2 text >> {}".format(a2.string))

# --------------------------------------------------------------------------------
print("\n---- 세 번째 a 태그 찾기")
a3 = a2.find_next_sibling("a")
print("a3 >> {}".format(a3))
print("a3 data-io >> {}".format(a3['data-io']))
print("a3 text >> {}".format(a3.string))
