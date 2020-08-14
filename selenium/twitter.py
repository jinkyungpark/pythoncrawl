from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = "d:/chromedriver/chromedriver.exe"
headless_options = webdriver.ChromeOptions()
# headless_options.add_argument("headless")
# 그래픽 카드 쓰지 않겠다
headless_options.add_argument("disable-gpu")
# 클라이언트 요청
headless_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
)

# 사용자가 쓰는 언어
headless_options.add_argument("lang=ko_KR")
# driver = webdriver.Chrome(chromedriver)
driver = webdriver.Chrome(chromedriver, options=headless_options)
# 전체 화면을 띄워야 함
driver.maximize_window()

driver.get("https://twitter.com/")
driver.implicitly_wait(2)

# 로그인 입력 창
userid = driver.find_element_by_name("session[username_or_email]")
userid.clear()
userid.send_keys("pjky5@naver.com")

userpwd = driver.find_element_by_name("session[password]")
userpwd.clear()
userpwd.send_keys("youjin0912*")
userpwd.send_keys(Keys.RETURN)

time.sleep(2)

#---------------------------------------- 트위터 로그인 종료
# 이 작업을 여러번 하다 보니 막혀버렸음


# 종료
driver.close()
