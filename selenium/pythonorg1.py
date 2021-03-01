from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 드라이버 생성
chromedriver = "./webdriver/chrome/chromedriver"
driver = webdriver.Chrome(chromedriver)
driver.implicitly_wait(2)
driver.maximize_window()

# ----------------------------------- 첫번째 테스트 종료

# 접속할 사이트 주소 넣어주기
driver.get("http://www.python.org")

print(driver.title)  # 웹 브라우저 타이틀 출력
# ----------------------------------- 두번째 테스트 종료

assert "Python" in driver.title  # driver.title 안에 Python 이라는 글씨가 없으면 에러를 발생시켜줘

# ----------------------------------- 세번째 테스트 종료


# ------------------------------------
# print(driver.page_source)
# -------------------------------------
print("===== 원하는 값 찾기")
elem = driver.find_element_by_name("q")
# input 텍스트 초기화
elem.clear()

# 키 이벤트 전송
elem.send_keys("python")
# 엔터 입력
elem.send_keys(Keys.RETURN)

# 돌아오는 페이지가 결과가 없다면 아래 작업은 할 필요가 없기 때문에
# 아래와 같은 구문 적용
assert "No results found." not in driver.page_source

# 크롤링 소스

driver.quit()
