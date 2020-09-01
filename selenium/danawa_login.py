from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests


# webdriver 설정
driver = webdriver.Chrome("d:/chromedriver/chromedriver.exe")

# 사이트 접속
driver.get("http://www.danawa.com/")
driver.implicitly_wait(2)


# 로그인 버튼 클릭
login = driver.find_element_by_css_selector(
    "div.my_service_list ul li.my_page_service a")

# 로그인 버튼 클릭
login.send_keys(Keys.RETURN)
driver.implicitly_wait(3)


# 아이디 input 얻어오기
userid = driver.find_element_by_id("danawa-member-login-input-id")
userid.clear()
userid.send_keys("pjky5")
driver.implicitly_wait(2)

# 비밀번호 input 얻어오기
userpwd = driver.find_element_by_id("danawa-member-login-input-pwd")
userpwd.clear()
userpwd.send_keys("12344321@a")
userpwd.send_keys(Keys.RETURN)
