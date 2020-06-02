# beautifulsoup 사용
# 스크랩핑 도구로 유명함
from bs4 import BeautifulSoup  # beautifulsoup4

# html 변수에 들어있는 값이 예를 들어 웹에서 가져온 소스라고 할 때

html = """
    <html>
        <head>
            <title>The Dormouse's story</title>
        </head>
        <body>
            <h1>this is h1 area</h1>
            <h2>this is h2 area</h2>
            <p class='title'><b>The Dormouse's story</b></p>
            <p class='story'>Once upon a time there were three little sistes.
                <a href='http://example.com/elsie' class='sister' id='link1'>Elsie</a>
                <a href='http://example.com/lacie' class='sister' id='link2'>Lacie</a>
                <a data-io="link3" href='http://example.com/little' class='sister' id='link3'>Title</a>
            </p>
            <p class='story'>
                story.....
            </p>
        </body>
    </html>
"""

# Beautifulsoup 단계
# bs4 초기화 - 웹에서 가져온 문서를 첫번째 인자로, 문서의 구조를 두번째 인자로
soup = BeautifulSoup(html, 'html.parser')

# 타입확인
print('soup', type(soup))  # soup <class 'bs4.BeautifulSoup'>
print('soup', soup.prettify())


# h1 태그 접근
print()
h1 = soup.html.body.h1
print(h1)

# 첫번째 p 태그 접근
print()
p1 = soup.html.body.p
print(p1)

# 두번째 p 태그 접근
# next_sibling : p 태그 다음의 공백 의미
print()
p2 = p1.next_sibling.next_sibling
print(p2.prettify())


# 학생들 실습 - 세번째 p 태그 접근
print()
p3 = p2.next_sibling.next_sibling
print(p3.prettify())


# 학생들 실습 - title 태그 출력하기
print()
title = soup.html.head.title
print(title)


# 가져온 태그가 가지고 있는 텍스트 출력
print()
print("h1 >>", h1.string)
print("p1 >>", p1.string)
print("p2 >>", p2.string)
print("p3 >>", p3.string)
print("title >>", title.string)


# 함수확인 - p2에서 사용가능한 함수들
# print(dir(p2))


# 반복 출력 확인 - p2의 다음 요소인 텍스트 엘리먼트 출력
print()
for v in p2.next_element:
    print(v, end='')  # end를 안 주면 글자 한자씩 나옴
