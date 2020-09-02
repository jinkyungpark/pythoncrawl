from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# webdrvier 로드
chromedriver = "d:/chromedriver/chromedriver.exe"

headless_options = webdriver.ChromeOptions()
headless_options.add_argument("headless")  # --headless 도 됨
# 그래픽 카드 쓰지 않겠다
headless_options.add_argument("disable-gpu")
# 클라이언트 요청
headless_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
)
# 브라우저 크기 지정
# headless_options.add_argument("window-size=1920x1080")
# 사용자가 쓰는 언어
headless_options.add_argument("lang=ko_KR")
driver = webdriver.Chrome(chromedriver, chrome_options=headless_options)

# 정보를 추출할 페이지 가져오기
driver.get(
    "https://news.mt.co.kr/mtview.php?no=2020081216310117937&outlink=1&ref=https%3A%2F%2Fsearch.daum.net"
)

# 페이지가 로드될 때까지 잠시 기다리기
driver.implicitly_wait(3)

# 전송된 페이지에서 원하는 값 추출하기
# class 이름을 가지고 하는 경우
title = driver.find_element_by_class_name("subject")

# 태그명으로는 로고가 h1을 쓰고 있어서 안나옴
# title = driver.find_element_by_tag_name("h1")
print(title.text)


# -----------------------------------------------------------------------제목 가져오기 종료
content = driver.find_element_by_id("textBody")
print(content.text)

# -----------------------------------------------------------------------내용 가져오기 종료

# <head> 태그 안 내용을 가져올 때는 get_attribute('text') 호출해야 함

head_title = driver.find_element_by_css_selector("head > title")
print(head_title.get_attribute("text"))
# ------------------------------------------------------------------------<head> 태그 안에 정보 추출

# 브라우저 종료
driver.quit()
