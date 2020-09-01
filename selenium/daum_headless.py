from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

headless_options = webdriver.ChromeOptions()
headless_options.add_argument("--headless")
# 웹 브라우저 사이즈 조절
headless_options.add_argument("window-size=1920x1080")
# 그래픽 카드 쓰지 않겠다
headless_options.add_argument("disable-gpu")
# 클라이언트 요청
headless_options.add_argument(
    "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
)
# 사용자가 쓰는 언어
headless_options.add_argument("lang=ko_KR")


driver = webdriver.Chrome(
    "d:/chromedriver/chromedriver.exe", options=headless_options
)


driver.get("https://www.daum.net")
print(driver.current_url)  # 현재 접속한 페이지 확인
assert "Daum" in driver.title

elem = driver.find_element_by_name("q")


elem.send_keys("아이폰")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source

# ---------------------------------------------------------------------------------------
top_list = driver.find_elements_by_css_selector(
    "div#recomm_lists_top > span.wsn"
)
for top in top_list:
    print(top.text)
