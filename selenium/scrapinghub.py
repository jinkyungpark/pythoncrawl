from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 드라이버 로드
driver = webdriver.Chrome("d:/chromedriver/chromedriver")

# 사이트 접속하기
driver.get("https://blog.scrapinghub.com/")

# 타이틀 확인
# print(driver.title)   # THE SCRAPINGHUB BLOG
assert "SCRAPINGHUB" in driver.title

# 검색 창 찾기
element = driver.find_element_by_class_name("hs-search-field__input")
print(element)
# 검색창에 scraping 이라는 키워드 넣고 페이지 이동
element.send_keys("scraping")
element.send_keys(Keys.RETURN)
time.sleep(5)


# 타이틀 추출하기
titles = driver.find_elements_by_css_selector("#hsresults li a")
for title in titles:
    print(title.text)


# 브라우저 종료
driver.quit()
