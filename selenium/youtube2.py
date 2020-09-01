# css_selector 이용한 정보 가져오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("d:/chromedriver/chromedriver.exe")

driver.get("https://www.youtube.com/")
assert "YouTube" in driver.title

# elem = driver.find_element_by_id("search") => 안됨
elem = driver.find_element_by_css_selector("input#search")

elem.send_keys("아이유")
elem.send_keys(Keys.RETURN)

# ---------------------------------------------------------------------------------------
time.sleep(3)
assert "No results found." not in driver.page_source

# #title-wrapper > h3  : h3 태그 선택하고 copy 해야 함
driver.find_elements_by_css_selector
titles = driver.find_elements_by_css_selector("#title-wrapper > h3")
for title in titles:
    print(title.text)
