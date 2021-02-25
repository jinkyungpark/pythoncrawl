# css 선택자 : select, select_one 이용하기
# 태그 선택자 : find, find_all
# select / select_one
# 태그 + 클래스 + 자식 선택자
from bs4 import BeautifulSoup  # beautifulsoup4

# html 변수에 들어있는 값이 예를 들어 웹에서 가져온 소스라고 할 때
with open("./beautiful/story.html", "r") as f1:
    html = f1.read()

# bs4 초기화 - 웹에서 가져온 문서를 첫번째 인자로, 문서의 구조를 두번째 인자로
soup = BeautifulSoup(html, 'html.parser')

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
print("****\n p.story > a\n")
print(link8)
# print(link8.string)  # 여러개를 가지고 오기 때문에 에러남
# print(link8.text) # 여러개를 가지고 오기 때문에 에러남

# 개별 a 태그로 출력
for link in link8:
    print(link)
    print(link.string)


# a 태그 두번째
link9 = soup.select('p.story > a:nth-of-type(2)')
print("***\n\n p.story > a:nth-of-type(2)\n")
print('link9', link9)

# p.story 를 가진 게 두 개가 있음
link10 = soup.select('p.story')
print("***\n\n p.story\n")
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


# 현재 html 문서의 모든 텍스트만 가져오려면?
print("텍스트 모두 출력")
print(soup.get_text())
