# 다음 댓글 가져오기 - 추천댓글 기본으로 설정되어 있는 상태(더보기 버튼이 한번만 나옴)
# Waits : 데이터들이 로드되는 시점의 차이가 존재하는 걸 처리
# implicit wait : 웹페이지 내의 요소를 찾기 위해 web driver가 일정시간 기다리도록 요청
# explicit wait : web driver가 실행을 계속하기 전에 특정 조건이 발생할 때까지 기다리는 것


# 특정 신문기사의 다음 댓글 가져오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 시간을 기다리기 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 마우스나 키보드를 조작하는 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

import time


chromedriver = "./webdriver/chrome/chromedriver"
headless_options = webdriver.ChromeOptions()
# headless_options.add_argument("headless")  # --headless 도 됨
# 그래픽 카드 쓰지 않겠다
headless_options.add_argument("disable-gpu")
# 클라이언트 요청
headless_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
)
# 브라우저 크기 지정
headless_options.add_argument("window-size=1920,1080")
# 사용자가 쓰는 언어
headless_options.add_argument("lang=ko_KR")
driver = webdriver.Chrome(chromedriver, chrome_options=headless_options)

# 정보를 추출할 페이지 가져오기
# 특정 기사를 가져오기
driver.get("https://news.v.daum.net/v/20200814162840083")

# 특정 기사에 딸린 댓글 가져오기
# ajax 로 넘어오는 데이터
loop, count = True, 0


# 다음 댓글은 20-08-14 현재 추천댓글이 먼저 보여지는 중
# 추천 댓글은 더보기 버튼이 한 번만 나옴
while loop and count < 10:
    try:  # 더보기 버튼을 기다리는 중
        element = WebDriverWait(driver, 5).until(
            # 해당 태그가 있는지 검사
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#alex-area > div > div > div > div.cmt_box > div.alex_more > button",
                )
            )
        )
        element.click()
        count += 1
        # 다음 더 보기 버튼이 나오기 전에 해당 태그가 있는지 검사하면 안되니까
        # 잠깐 기다리기
        time.sleep(2)
    except TimeoutException:
        loop = False


driver.quit()

