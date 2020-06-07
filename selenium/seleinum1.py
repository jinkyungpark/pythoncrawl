# Selenium
# Selenium 사용 실습

# 설정 및 기본 테스트
# selenium 임포트
from selenium import webdriver

# webdriver 설정
browser = webdriver.Chrome('./webdriver/chrome/chromedriver.exe')

# ------------------------ (웹드라이버 구동 여부)

# 크롬 브라우저 내부 대기
# 인터넷 속도가 서로 다르고 컴퓨터 환경이 다르기 때문에 시간을 줘야 함
browser.implicitly_wait(5)  # 5초(일반적인 코드임)
# print(dir(browser))  # 사용할 수 있는 함수 알아보기

# 브라우저 크기 
# 브라우저 크기를 지정하지 않은 경우 조금 전 띄웠던 브라우저 크기로 띄워짐
browser.maximize_window() # 모니터 크기에 꽉차는 브라우저 크기 생성  

# browser.set_window_size(500,400) # 특정 크기로 브라우저 띄우고 싶다면

# -----------------------(브라우저 사이즈)

# 브라우저 이동
browser.get("https://www.daum.net/")

# print('page Contents : {}'.format(browser.page_source))


# ---------------------- (소스 가져오기)

print()
print('Session ID : {}'.format(browser.session_id))
print('Title : {}'.format(browser.title))
print('URL : {}'.format(browser.current_url))
print('Cookies : {}'.format(browser.get_cookies))



