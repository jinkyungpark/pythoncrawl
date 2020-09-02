from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# exe 생략가능
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(
    "d:/chromedriver/chromedriver.exe", chrome_options=options)
driver.implicitly_wait(3)

driver.get("https://www.daum.net")

# ---------------------------------------------------------- 1차 확인

print(driver.current_url)
print(driver.title)
assert "Daum" in driver.title

# ---------------------------------------------------------- 2차 확인

# print(driver.page_source)


# ---------------------------------------------------------- 3차 확인

print()
print('Session ID : {}'.format(driver.session_id))
print('Title : {}'.format(driver.title))
print('URL : {}'.format(driver.current_url))
print('Cookies : {}'.format(driver.get_cookies))

# ------------------------------------------------------------
driver.quit()
