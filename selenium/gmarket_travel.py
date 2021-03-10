# gmarket 여행 베스트에서 하나의 제품을 클릭하고 들어가서
# 여행 상품명 클릭

from selenium import webdriver
import time
from selenium.webdriver.common.by import By   # wait 시 필요
from selenium.webdriver.support.ui import WebDriverWait  # 브라우저가 다 로딩될 때 기다려줌
# 어떤 상태가 될때까지 기다려주기 위해 필요
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 크롬 브라우저 옵션 설정
chrome_options = Options()
# 이전까지 브라우저가 실행됐다가 꺼지는 상태였기 때문에 안하기 위해
# chrome_options.add_argument("--headless")

# 웹 드라이버 로드 -- Headless 모드(개발 다 하고 변경)
browser = webdriver.Chrome(
    "./webdriver/chrome/chromedriver.exe", options=chrome_options)

browser.get("http://gtour.gmarket.co.kr/TourV2/Item?GoodsCode=1597099569")


# print(browser.page_source)

WebDriverWait(browser, 3).until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "h1.itemtit")))

soup = BeautifulSoup(browser.page_source, "html.parser")

# print(soup)
print(soup.select_one("h1.itemtit").text)

time.sleep(3)
