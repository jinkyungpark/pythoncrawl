# http://pythonscraping.com/pages/page3.html : 해당 페이지 스크랩핑

from bs4 import BeautifulSoup
import requests


# url 지정
url = "http://pythonscraping.com/pages/page3.html"

res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

# [실습1] Totally Normal Gifts 가져온 후 출력하기
h1 = soup.find('h1')
print(h1)  # <h1>Totally Normal Gifts</h1>
print(h1.string)   # Totally Normal Gifts
print(h1.get_text())   # Totally Normal Gifts


# [실습2] 상단의 내용 출력하기
# content = soup.find('div', attrs={'id': 'content'})
# print(content.get_text())


# [실습3] 모든 img 태그 수집한 후 출력하기
# img_all_list = soup.select("img")
# print(img_all_list)

# [실습4] 모든 img 태그 수집한 후 출력하기(단 로고 제외)
# 'image[src="../img/gifts/logo.jpg"]'
# img_list = soup.select("tr.gift > td > img")
# for img in img_list:
#     print(img)


# [실습5] 테이블 내용 출력하기
child = soup.find("table", {"id": "giftList"}).children
for c in child:
    print(c)

# [실습6] 타이틀 행 다음에 모든 행 수집하기
# siblings = soup.find("table", {"id": "giftList"}).tr.next_siblings
# for s in siblings:
#     print(s)

# [실습7] 가격만 가지고 오기
print()
list = soup.find_all("tr", class_="gift")
for ch in list:
    # print(ch)
    print(ch.find_all("td")[2].text)
    print("------------")
