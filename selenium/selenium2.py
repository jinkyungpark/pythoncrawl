from selenium import webdriver

browser = webdriver.Chrome('./webdriver/chrome/chromedriver')

browser.implicitly_wait(5)
browser.maximize_window()
browser.get('https://www.daum.net')


# 검색창 input 선택 -  find_elements 도 있음(주의)
element = browser.find_element_by_css_selector(
    'div.inner_search > input.tf_keyword')

# 검색어 입력하기
element.send_keys('방탄소년단')

# submit 을 위한 엔터 기능
element.submit()

# -------------------------------------- 자동화된 검색기능 구현


# 스크린 샷 저장1
browser.save_screenshot('c:/website_ch1.png')

browser.get_screenshot_as_file('c:/website_ch2.png')

# 브라우저 종료 - 브라우저가 닫히긴 하지만 완벽한 종료를 위해
browser.quit()
