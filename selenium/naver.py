from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("./webdriver/chrome/chromedriver")
driver.implicitly_wait(2)

# 주소를 잘못 쓰면 여기에서 이미 에러 발생
driver.get("https://www.naver.com")
assert "NAVER" in driver.title

elem = driver.find_element_by_name("query")

elem.send_keys("갤럭시")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
# ---------------------------------------------------------------------------------------
time.sleep(2)
driver.quit()
