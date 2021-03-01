from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("./webdriver/chrome/chromedriver")
driver.implicitly_wait(3)

# 특정 사이트 접속
driver.get("https://www.daum.net")


print(driver.current_url)  # 현재 접속한 페이지 확인
assert "Daum" in driver.title

# ---------------------------------------------------------- 2차 확인

# 접속한 사이트에서 페이지 정보 가져오기
# print(driver.page_source)

# ---------------------------------------------------------- 3차 확인

elem = driver.find_element_by_name("q")


elem.send_keys("아이폰")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source


# 넘어온 데이터를 가지고 크롤링 하기

driver.quit()
