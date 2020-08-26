import requests
from bs4 import BeautifulSoup

res = requests.get('https://news.v.daum.net/v/20200630183248931')
soup = BeautifulSoup(res.content, 'html.parser')

# print(soup.prettify())

# 뉴스 제목 가져오기
title = soup.find('h3')
print('제목 : %s' % title.get_text())

# 기사 작성자 가져오기
print('작성자 : %s' % soup.find('span', 'txt_info').get_text())
print("작성자 : {}".format(soup.select_one("span[class='txt_info']").string))

# 기사 작성 시간
print('작성시간 : %s' % soup.find('span', 'num_date').get_text())
print("작성시간 : {}".format(soup.select_one("span[class='num_date']").string))

# 기사의 첫번째 문단 가져오기
print('첫번째 문단 : %s' %
      soup.find('p', attrs={'dmcf-ptype': 'general'}).get_text())

# 첫번째 문단에서 css selector를 가져오는 건 안 되서 그 위의 부분을 잡아서 처리함
#harmonyContainer > section
print('첫번째 문단 : %s' %
      soup.select_one("#harmonyContainer > section > p").get_text())

# p_content = soup.find_all("p", attrs={'dmcf-ptype': 'general'})
# print(p_content)
# for item in p_content:
#     print(item.get_text())
