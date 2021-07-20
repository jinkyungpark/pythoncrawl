import requests
from bs4 import BeautifulSoup
import re

response = requests.get("https://www.daum.net/")

soup = BeautifulSoup(response.content,"html.parser")

# h로 시작하는 태그 찾기
print(soup.find_all(re.compile("h\d")))

# 이미지 파일만 찾아오기
print(soup.find_all('img',attrs={'src': re.compile('.+\.jpg')}))
print(soup.find_all('img',attrs={'src': re.compile('.+\.(jpg|png)')}))
