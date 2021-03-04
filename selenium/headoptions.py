from selenium import webdriver


chromedriver = "./webdriver/chrome/chromedriver"

options = webdriver.ChromeOptions()
# 브라우저 안 띄우기
options.add_argument("--headless")
# 그래픽 카드 안 쓰기
options.add_argument("disable-gpu")
# 클라이언트 세팅하기
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
)
# 브라우저 크기 지정
options.add_argument("window-size=1920x1080")
# 사용자가 쓰는 언어
options.add_argument("lang=ko_KR")
driver = webdriver.Chrome(chromedriver, chrome_options=options)


# 사이트 접속
driver.get("http://www.daum.net")

print(driver.title)
