from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome('./webdriver/chrome/chromedriver')

browser.implicitly_wait(2)
browser.maximize_window()

browser.get('https://www.daum.net')
assert "Daum" in browser.title

# 검색창 input 선택 -  find_elements 도 있음(주의)
element = browser.find_element_by_css_selector(
    'div.inner_search > input.tf_keyword')

# 검색어 입력하기
element.send_keys('방탄소년단')

# submit 을 위한 엔터 기능
# element.submit()
element.send_keys(Keys.RETURN)

time.sleep(3)
assert "No results found." not in browser.page_source
# -------------------------------------- 자동화된 검색기능 구현

# 스크린 샷 저장1 -  확장자 선택 가능
browser.save_screenshot('c:/website_ch1.jpg')

# 현재 창을 png 이미지로 저장 => png로 확장자를 주지 않으면
# 에러 발생
browser.get_screenshot_as_file('c:/website_ch2.png')

# 브라우저 종료 - 브라우저가 닫히긴 하지만 완벽한 종료를 위해
browser.quit()
