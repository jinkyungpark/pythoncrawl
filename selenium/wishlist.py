from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

# webdriver 설정
driver = webdriver.Chrome("d:/chromedriver/chromedriver.exe")
driver.implicitly_wait(5)
driver.maximize_window()

# 사이트 접속
driver.get("http://www.danawa.com/")


# 로그인 버튼 클릭
login = driver.find_element_by_css_selector(
    "div.my_service_list ul li.my_page_service a")

# 로그인 버튼 클릭
login.send_keys(Keys.RETURN)
driver.implicitly_wait(3)


# 아이디 input 얻어오기
userid = driver.find_element_by_id("danawa-member-login-input-id")
userid.clear()
userid.send_keys("pjky5")
driver.implicitly_wait(2)

# 비밀번호 input 얻어오기
userpwd = driver.find_element_by_id("danawa-member-login-input-pwd")
userpwd.clear()
userpwd.send_keys("12344321@a")
userpwd.send_keys(Keys.RETURN)

# -------------------------------------------------------------------------- 로그인 성공


# ---------------------------------------------------------------------------
# 검색 창 얻어오기
search = driver.find_element_by_id("AKCSearch")
search.clear()
search.send_keys("세탁기")
search.send_keys(Keys.RETURN)


# 페이지가 로드될 때까지 기다리기
time.sleep(3)

# 제조사별, 에너지 등급, 품목, 세탁 용량 click

# 제조사별 클릭 - LG전자
driver.find_element_by_xpath(
    "//*[@id='SearchOption_Maker_Rep']/div[1]/div/label/span[1]").click()

# 에너지 등급 클릭 - 1등급
driver.find_element_by_xpath(
    "//*[@id='SearchOption_BasicOption_21088_All']/div[1]/div/label/span").click()

# 품목 클릭 - 드럼세탁기
driver.find_element_by_xpath(
    "//*[@id='newSearchOptionArea']/div[2]/div[2]/div[4]/div[1]/div[2]/div[1]/div[5]/div/label/span").click()

# 세탁 용량 더보기 버튼 기다리기
# //*[@id="newSearchOptionArea"]/div[2]/div[2]/div[6]/div[1]/div[2]/div[2]/button[1]
# WebDriverWait(driver, 3).until(EC.presence_of_element_located(
#     (By.XPATH, "//*[@class='so_cont_area']/div[6]/div/div[2]/div[2]/button[1]"))).click()

# ElementClickInterceptedException 발생한다면
WebDriverWait(driver, 3).until(EC.presence_of_element_located(
    (By.XPATH, "//*[@class='so_cont_area']/div[6]/div/div[2]/div[2]/button[1]"))).send_keys(Keys.ENTER)


# 그 중에서 18kg 클릭
# //*[@id="SearchOption_RepOption_92_All"]/div/div[5]/div/label/span
WebDriverWait(driver, 3).until(EC.presence_of_element_located(
    (By.XPATH, "//*[@id='SearchOption_RepOption_92_All']/div/div[5]/div/label/span"))).click()

time.sleep(2)

# ----------------------------------------------------------------------------- 테스트

# 첫번째 상품 클릭하여 상세 페이지 들어가기 - 새 창으로 뜸
driver.find_element_by_css_selector(
    "#productItem11772502 > div > div.prod_info > p > a").click()

# 새 창으로 제어권 넘기기
driver.switch_to.window(driver.window_handles[1])

# 관심 버튼이 생길 때까지 잠시 기다리기
# time.sleep(3)
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#interest > span.ico.ico_interest"))).click()

# 어디에 담을 것인지 보여주는 리스트 나올 때까지 기다리기
WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                               "#btn_bundle > div > dl.wish_folder > dd > ul > li"))).click()
# 관심상품 리스트로 가기 클릭
driver.find_element_by_css_selector(
    "#btn_bundle > div > div > div > a").click()

time.sleep(3)

# 관심상품 리스트 출력하기
soup = BeautifulSoup(driver.page_source, "html.parser")

wishlist = soup.select("table.wish_tbl > tbody > tr")

for idx, item in enumerate(wishlist, 1):
    # item => tr 하나를 의미
    # print("item: {}".format(item))

    product_name = item.select_one("td.info > div.tit > a").text
    product_spec = item.select_one("dl.spec > dd > a").text
    product_price = item.select_one("td.lowest > dl > dd > span").text

    print("[{}] {}".format(idx, product_name))
    print("{}".format(product_spec))
    print("{}".format(product_price))
    print()

# ------------------------------------------------------------------------------ 확인
time.sleep(5)
driver.close()
