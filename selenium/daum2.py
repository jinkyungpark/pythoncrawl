from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("d:/chromedriver/chromedriver.exe")


driver.get("https://www.daum.net")
# print(driver.title)
assert "Daum" in driver.title

print(driver.page_source)
