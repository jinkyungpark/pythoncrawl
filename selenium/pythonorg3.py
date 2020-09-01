# 다양한 선택자 사용하기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# 드라이버 생성
chromedriver = "d:/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)
# ---------------------------------------------------------------------------------------
# 접속할 사이트 주소 넣어주기
driver.get("http://www.python.org")
assert "Python" in driver.title
# ---------------------------------------------------------------------------------------
# 검색어에 python 넣고 결과 보기

# 해당 태그를 아이디 값으로 찾기
# elem = driver.find_element_by_id("id-search-field")

# 해당 태그를 css 선택자로 찾기
# elem = driver.find_element_by_css_selector("input#id-search-field")

# 해당 태그를 클래스 이름으로 찾기
# elem = driver.find_element_by_class_name("search-field")

# 해당 태그를 xpath 로 찾기 //*[@id="id-search-field"] 요소에 가서 copy 값 가지고 옴
elem = driver.find_element_by_xpath("//*[@id='id-search-field']")

# elem = driver.find_element_by_id("id-search-field")
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
time.sleep(5)

# 검색결과를 받아와서 출력하기
titles = driver.find_elements_by_tag_name("h3")
for title in titles:
    print(title.text)

# 크롬 브라우저 닫기
driver.quit()
