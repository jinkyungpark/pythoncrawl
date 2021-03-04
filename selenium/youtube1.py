from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("./webdriver/chrome/chromedriver")
# driver.implicitly_wait(5) # 꼭 필요한 것은 아님

driver.get("https://www.youtube.com/")
assert "YouTube" in driver.title


elem = driver.find_element(By.NAME, "search_query")
# elem = driver.find_element_by_name("search_query")


elem.send_keys("아이유")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

# ---------------------------------------------------------------------------------------

time.sleep(2)

titles = driver.find_elements(By.TAG_NAME, "h3")
# titles = driver.find_elements_by_tag_name("h3")
for title in titles:
    print(title.text)
