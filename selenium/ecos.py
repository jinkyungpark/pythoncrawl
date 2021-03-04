from selenium import webdriver
import time


driver = webdriver.Chrome("./webdriver/chrome/chromedriver")
driver.implicitly_wait(3)


# 100대 통계지표 클릭 - frameset 안에 구성되어 있음
# 따라서 첫 페이지를 요청할 때 http://ecos.bok.or.kr 이렇게 요청하면 버튼을 못 찾음
driver.get("http://ecos.bok.or.kr/EIndex.jsp")
driver.implicitly_wait(3)


driver.find_element_by_css_selector(
    "div.ESsubject > ul > li:nth-child(1) > a").click()
time.sleep(2)

# 새창으로 제어 넘기기
driver.switch_to.window(driver.window_handles[1])
driver.implicitly_wait(2)

# 새 창에서 엑셀 다운로드 클릭
driver.find_element_by_css_selector(
    "div.HScontent-header > div > fieldset > a > img").click()

time.sleep(2)

driver.close()
