import requests
from bs4 import BeautifulSoup
import re

response = requests.get("https://www.daum.net/")

soup = BeautifulSoup(response.content,"html.parser")

print(soup.find_all(re.compile("h\d")))
