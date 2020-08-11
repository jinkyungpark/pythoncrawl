from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("d:/chromedriver/chromedriver.exe")

driver.get("https://www.naver.com")
assert "NAVER" in driver.title

elem = driver.find_element_by_name("query")

elem.send_keys("갤럭시")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

# ---------------------------------------------------------------------------------------
