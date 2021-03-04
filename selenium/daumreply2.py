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


# 최신순 클릭하기

# 최신순 버튼이 보여질때까지 기다린 후 클릭하기
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.CSS_SELECTOR, "div.cmt_box > ul > li:nth-child(3)")
    )
).click()


# 특정 기사에 딸린 댓글 가져오기
# ajax 로 넘어오는 데이터
loop, count = True, 0


# 다음 댓글은 20-08-14 현재 추천댓글이 먼저 보여지는 중
# 최신순 댓글은 더보기 버튼 반복
while loop and count < 10:
    try:  # 더보기 버튼을 기다리는 중
        element = WebDriverWait(driver, 3).until(
            # 해당 태그가 있는지 검사
            EC.presence_of_element_located(
                (
                    By.CSS_SELECTOR,
                    "#alex-area > div > div > div > div.cmt_box > div.alex_more > button",
                )
            )
        )
        more_button = driver.find_element_by_css_selector(
            "#alex-area > div > div > div > div.cmt_box > div.alex_more > button"
        )
        webdriver.ActionChains(driver).click(more_button).perform()
        count += 1
        # 다음 더 보기 버튼이 나오기 전에 해당 태그가 있는지 검사하면 안되니까
        # 잠깐 기다리기
        time.sleep(2)
    except TimeoutException:
        loop = False


driver.quit()
