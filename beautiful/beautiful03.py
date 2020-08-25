# beautifulsoup 사용
# 스크랩핑 도구로 유명함

from bs4 import BeautifulSoup  # beautifulsoup4

# html 변수에 들어있는 값이 예를 들어 웹에서 가져온 소스라고 할 때
with open("./beautiful/story.html", "r") as f1:
    html = f1.read()

# Beautifulsoup 단계
# bs4 초기화 - 웹에서 가져온 문서를 첫번째 인자로, 문서의 구조를 두번째 인자로
soup = BeautifulSoup(html, 'html.parser')

# a 태그 찾기
a = soup.find_all('a')
print(a)

# a 태그가 여러개 있을 경우 앞에서 2개만 가져오기
print()
a = soup.find_all('a', limit=2)
print(a)

# a 태그가 많다면 find_all() 이 너무 많을 수 있기는 함

# 태그가 가지고 있는 속성 값으로 가져오기

# 클래스 이름으로 가져오기
print("----")
link2 = soup.find_all("a", class_='sister')
print(link2)

# 텍스트 노드 값이 Elsie인 것 찾아오기
print("****")
link2 = soup.find_all("a", string=["Elsie"])
print(link2)

# 텍스트 노드가 Elsie인 노드와 Title인 것 가져오기
print()
link2 = soup.find_all("a", string=["Elsie", "Tillie"])
print(link2)


# 처음 발견한 a 태그 선택
link3 = soup.find("a")
print()
print(link3)
print(link3.string)  # 문자열 출력
print(link3.text)   # 문자열 출력

# 다중조건
link4 = soup.find("a", {"class": "sister", "data-io": "link3"})
print()
print(link4)


# css 선택자 : select, select_one 이용하기
# 태그 선택자 : find, find_all
# select / select_one
# 태그 + 클래스 + 자식 선택자
link5 = soup.select_one('p.title > b')
print()
print(link5)
print(link5.string)
print(link5.text)

# id가 link1인 태그 가져오기
link6 = soup.select_one("a#link1")
print()
print(link6)
print(link6.string)
print(link6.text)

# 속성을 이용하여 태그 가져오기
link7 = soup.select_one("a[data-io='link3']")
print()
print(link7)
print(link7.string)
print(link7.text)

# 전체 선택
link8 = soup.select("p.story > a")
print()
print(link8)
# print(link8.string) 여러개를 가지고 오기 때문에 에러남
# print(link8.text)


# a 태그 두번째
link9 = soup.select('p.story > a:nth-of-type(2)')
print()
print('link9', link9)

# p.story 를 가진 게 두 개가 있음
link10 = soup.select('p.story')
print()
print(link10)


# 위의 예에서 만일 string 출력을 하고 싶다면?
for t in link10:
    temp = t.find_all('a')

    if temp:
        for v in temp:
            print('>>>>>', v)
            print('>>>>>', v.string)
    else:
        print('-----', t)
        print('-----', t.string)
