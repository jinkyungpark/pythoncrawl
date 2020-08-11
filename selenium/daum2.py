from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("d:/chromedriver/chromedriver.exe")


driver.get("https://www.daum.net")
# print(driver.title)
assert "Daum" in driver.title

elem = driver.find_element_by_name("q")

elem.send_keys("아이폰")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

# ---------------------------------------------------------------------------------------

# time.sleep(2)
