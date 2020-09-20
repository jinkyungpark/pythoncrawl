from selenium import webdriver
import time
from bs4 import BeautifulSoup

# webdrvier 로드
chromedriver = "d:/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(chromedriver)
# 정보를 추출할 페이지 가져오기
driver.get("https://www.daum.net/")
time.sleep(3)

# 전송된 페이지에서 원하는 값 추출하기
# 다음 메인 페이지에서 맨 좌측에 있는 신문기사 클릭하여 사이트 들어가기
article = driver.find_element_by_css_selector(
    "ul.list_thumb > li > a > div.cont_item")
article.click()

# ele = driver.find_element_by_css_selector("div.head_view > h3")
# print(ele.text)

# beautifulsoup 으로 처리하기
soup = BeautifulSoup(driver.page_source, "html.parser")

title = soup.select_one("div.head_view > h3")
print(title.text)


time.sleep(3)

# 브라우저 종료
driver.quit()
