from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 드라이버 로드
driver = webdriver.Chrome("d:/chromedriver/chromedriver")
driver.maximize_window()
# 사이트 접속하기
driver.get("http://sll.seoul.go.kr/")

# 타이틀 확인
print(driver.title)   # THE SCRAPINGHUB BLOG
assert "서울시평생학습포털" in driver.title

# 통합검색 클릭
driver.find_element_by_id("search_btn").click()

# 큰 검색창이 뜨면 그 안에 영어 검색어 넣고 엔터
element = driver.find_element_by_id("query")

element.send_keys("영어")

time.sleep(2)

element.send_keys(Keys.RETURN)

# 검색결과가 새창으로 뜨는 시간 기다리기
time.sleep(3)


# 최근 열린 탭으로 전환 driver.window_handles[0]  => 현재 창
driver.switch_to.window(driver.window_handles[1])


# 로딩 기다리기
print("new window : {}".format(driver.current_url))

# 더 많은 결과보기 클릭
more = driver.find_element_by_css_selector(
    "div.search-result-title > a.btn-more-result").click()

time.sleep(5)

# 브라우저 종료
driver.quit()
