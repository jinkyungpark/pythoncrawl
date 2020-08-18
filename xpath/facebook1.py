from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 시간을 기다리기 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 마우스나 키보드를 조작하는 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

chromedriver = "d:/chromedriver/chromedriver.exe"

driver = webdriver.Chrome(chromedriver)
driver.get("https://www.facebook.com/")


email_path = "//*[@id='email']"
pass_path = "//*[@id='pass']"
# button_path 찾을 때 로그인을 한 번 한 후에 다음부터 들어가는 페이지에서
# 버튼의 path는 //*[@id='u_0_f'] 임 이렇게 찾으면 TimeoutException 발생함
button_path = "//*[@id='u_0_b']"

try:
    # 해당 태그가 생길때까지 기다리고
    email_tag = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, email_path)))
    pass_tag = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, pass_path)))
    login_btn = WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, button_path)))

    email_tag.clear()
    email_tag.send_keys("pjky5@naver.com")
    pass_tag.clear()
    pass_tag.send_keys("thsdbwls25*")
    # pass_tag.send_keys(Keys.RETURN)  로그인에서 엔터
    login_btn.click()

    time.sleep(5)
except TimeoutException as e:
    print(e)


driver.quit()
