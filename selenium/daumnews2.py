from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# webdrvier 로드
chromedriver = "d:/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

# 정보를 추출할 페이지 가져오기
driver.get("https://www.daum.net/")

# 전송된 페이지에서 원하는 값 추출하기
# 다음 메인 페이지에서 맨 좌측에 있는 신문기사 클릭하여 사이트 들어가기
article = driver.find_element_by_css_selector("ul.list_thumb > li")
article.click()

time.sleep(3)

# 브라우저 종료
driver.quit()
