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
