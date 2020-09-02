from selenium import webdriver
import time

# 드라이버 로드
driver = webdriver.Chrome("d:/chromedriver/chromedriver")
driver.maximize_window()
# 사이트 접속하기
driver.get("https://google.com")

# 타이틀 확인
print("현재 창 : {}".format(driver.title))

# 부모 창 정보 가져오기
parent_window = driver.current_window_handle

# 자바스크립트로 새로운 창 열기
driver.execute_script("window.open('https://www.naver.com')")

# driver.window_handles : 현재 브라우저에 열린 모든 창의 정보
all_windows = driver.window_handles

# 자식 창에 대한 정보 가져오기
child_window = [window for window in all_windows if window != parent_window][0]
print("child_window info : {}".format(child_window))

# 자식 창으로 제어권 이동
driver.switch_to_window(child_window)
print("현재 창 : {}".format(driver.title))

time.sleep(3)

# 자식창 닫기
driver.close()

# 부모 창으로 제어권 이동
# driver.switch_to_window() 쓰면 지워졌다고 . 으로 변경하라 함
driver.switch_to.window(parent_window)
print(driver.title)

time.sleep(5)

# 부모창 닫기
driver.close()
