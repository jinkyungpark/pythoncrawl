from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./webdriver/chrome/chromedriver")


# 주소를 잘못 쓰면 여기에서 이미 에러 발생
driver.get("https://www.gmarket.co.kr/")
time.sleep(3)

elem = driver.find_element_by_name("keyword")

elem.send_keys("아이폰")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# ---------------------------------------------------------------------------------------
time.sleep(2)
driver.quit()  # 세션 종료
