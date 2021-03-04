from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait

# 서울시 평생학습 포털 사이트에서 영어 와 관련된
# 과정 추출하기 - 팝업창 닫기와 WebdriverWait 사용

# 웹드라이버 로드
driver = webdriver.Chrome("./webdriver/chrome/chromedriver")
driver.maximize_window()

driver.implicitly_wait(3)

# 정보를 추출할 사이트 접속하기
driver.get("http://sll.seoul.go.kr/")

# 테스트 코드 삽입
assert "서울시평생학습포털" in driver.title

# 팝업창 닫기
popups = driver.find_elements_by_name("btn_layer_popup_close")
for pop in popups:
    pop.click()

try:
    # 통합검색창 클릭 -> 영어 입력 후 엔터
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".a-search-box > span"))
    )
    search.click()

    element = driver.find_element_by_id("query")
    element.send_keys("영어")
    element.send_keys(Keys.RETURN)

    # 새 창으로 제어 넘기기
    driver.switch_to.window(driver.window_handles[-1])
    # 새 창으로 제어가 넘어갔는지 확인
    print(driver.current_url)

    # 더 많은 결과 보기 클릭
    driver.find_element_by_css_selector(
        "div.search-result-title > a.btn-more-result"
    ).click()

    # 결과 페이지에서 강좌명 출력
    subjects = driver.find_elements_by_css_selector(
        "div.search-result-list > ul > li > div > a"
    )

    for title in subjects:
        print(title.text)

    time.sleep(3)
except TimeoutException as e:
    print(e)
# 종료
driver.quit()
