# 설정 및 기본 테스트
# selenium 임포트
from selenium import webdriver

# webdriver 설정
driver = webdriver.Chrome('./webdriver/chrome/chromedriver')

# 크롬 브라우저 내부 대기
# 인터넷 속도가 서로 다르고 컴퓨터 환경이 다르기 때문에 시간을 줘야 함
driver.implicitly_wait(5)  # 5초(일반적인 코드임)
# print(dir(driver))  # 사용할 수 있는 함수 알아보기

# 브라우저 크기
# 브라우저 크기를 지정하지 않은 경우 조금 전 띄웠던 브라우저 크기로 띄워짐
driver.maximize_window()  # 모니터 크기에 꽉차는 브라우저 크기 생성

# driver.set_window_size(500,400) # 특정 크기로 브라우저 띄우고 싶다면

# -----------------------(브라우저 사이즈)
