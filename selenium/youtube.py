from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("d:/chromedriver/chromedriver.exe")


driver.get("https://www.youtube.com/")
assert "YouTube" in driver.title

elem = driver.find_element_by_name("search_query")


elem.send_keys("아이유")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

# ---------------------------------------------------------------------------------------

time.sleep(2)
titles = driver.find_elements_by_tag_name("h3")
for title in titles:
    print(title.text)

