from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("d:/webdriver/chromedriver.exe")

driver.get("https://www.facebook.com/")

# id xpath = "//*[@id='email']"
# password xpath = "//*[@id='pass']"

email_path = driver.find_element_by_xpath("//*[@id='email']")
pass_path = driver.find_element_by_xpath("//*[@id='pass']")

# 로그인 시도
email_path.clear()
email_path.send_keys("pjky5@naver.com")
pass_path.clear()
pass_path.send_keys("thsdbwls25*")
pass_path.send_keys(Keys.RETURN)

time.sleep(5)
driver.quit()
