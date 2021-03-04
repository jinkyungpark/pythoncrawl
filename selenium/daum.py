from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# exe 생략가능
driver = webdriver.Chrome("./webdriver/chrome/chromedriver")

driver.get("https://www.daum.net/")
driver.implicitly_wait(3)

# ---------------------------------------------------------- 1차 확인

print(driver.current_url)
print(driver.title)
assert "Daum" in driver.title

# ---------------------------------------------------------- 2차 확인

# print(driver.page_source)


# ---------------------------------------------------------- 3차 확인

# 해당 요소 찾기
element = driver.find_element(By.NAME, "q")
# 찾은 요소에 검색어 넣기
element.send_keys("안드로이드")
element.send_keys(Keys.ENTER)

# 뒤로가기
driver.back()

# 현재 윈도우 핸들 얻기
print(driver.current_window_handle)  # CDwindow-7FCD8FFCC4FC00B67F80ED9F89D5E233
# Opens a new tab and switches to new tab
driver.switch_to.new_window('tab')

# Opens a new window and switches to new window
# driver.switch_to.new_window('window')


# ------------------------------------------------------------

time.sleep(3)
driver.quit()
