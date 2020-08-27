from bs4 import BeautifulSoup
import requests


res = requests.get("http://www.gmarket.co.kr")

soup = BeautifulSoup(res.text, "html.parser")
# print(soup)

# 1 depth category 추출
ul_list = soup.find("ul", class_="list__category-all")
one_depth = ul_list.find_all("span", "link__1depth-item")

# 아래 방식으로만 끌면 이런 태그를 가진게 한 번 더 있어서 두 번 나옴
# limit 를 줘서 제한 걸어야 함
# one_depth = soup.find_all("span", "link__1depth-item", limit=9)

# for item in one_depth:
#     print(item)

# ----------------------------------------------------------------------

# 2 depth category 추출
link__1depth = soup.find_all("li", "list-item__2depth")
for depth in link__1depth:
    print(depth)
# print(type(link__1depth))   # <class 'bs4.element.ResultSet'>

# 2depth에서 카테고리 주소와 카테고리 명만 추출
for depth in link__1depth:
    link1 = depth.find("a")['href']
    print(link1, depth.string)
