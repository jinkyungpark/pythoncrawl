from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 드라이버 생성
chromedriver = "d:/chromedriver/chromedriver.exe"
headless_options = webdriver.ChromeOptions()
headless_options.add_argument("headless")
driver = webdriver.Chrome(chromedriver, options=headless_options)

# 접속할 사이트 주소 넣어주기
driver.get("http://www.python.org")

# 웹 브라우저 타이틀 확인
# print(driver.title)

# 사이트 잘 접속되었는지 확인
# title 안에 python 들어 있어야 돼
assert "Python" in driver.title

# print(driver.page_source)
# 돌아오는 페이지가 결과가 없다면 아래 작업은 할 필요가 없기 때문에
# 아래와 같은 구문 적용


# ---------------------------------------------------------------------------------------
# 검색어에 python 넣고 결과 보기

# 해당 태그를 이름으로 찾기
elem = driver.find_element_by_name("q")
# input 텍스트 초기화
elem.clear()

# 키 이벤트 전송
elem.send_keys("python")
# 엔터 입력
elem.send_keys(Keys.RETURN)

# 소스 안에 이 내용이 들어 있지 않아야 해
assert "No results found." not in driver.page_source
# ---------------------------------------------------------------------------------------
# 검색어 넣고 엔터 친 후 결과가 보여지는 경우 테스트 - 2. find_elements_by_tag_name

# 명시적으로 일정시간을 기다릴 수 있음
# 검색어를 넣고 2초 기다릴게
time.sleep(2)

# 검색결과를 받아와서 출력하기
titles = driver.find_elements_by_tag_name("h3")
for title in titles:
    print(title.text)


# 크롬 브라우저 닫기
driver.quit()
