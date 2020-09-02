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
chrome_options.add_argument("--headless")

# 웹 드라이버 로드 -- Headless 모드(개발 다 하고 변경)
browser = webdriver.Chrome(
    "d:/chromedriver/chromedriver.exe", options=chrome_options)

# -------------------------- 확인(브라우저가 안 뜨는지 확인)

# browser = webdriver.Chrome("./webdriver/chrome/chromedriver.exe")

# 크롬 브라우저 내부 대기
browser.implicitly_wait(5)   # 여유있게 기다리겠다
browser.set_window_size(1080, 1024)

# 페이지 이동 - 실제 브라우저로 동작시켜 주소 얻어내기
browser.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

# -------------------------- 확인(노트북 페이지까지 들어간 후 화면이 닫히는 지 확인)

# 1차 페이지 이동
# print('Before Page Contents : {}'.format(browser.page_source))


# --------------------------- 확인(페이지 소스가 나오는지 확인)


# 제조사별 더 보기 클릭1
# 새로고침 후 페이지가 다 로드되는 시간만큼 명시적으로 기다리기
# WebDriver가 기다릴거야 브라우저가 3초간
# 사용자가 선택하려고 하는 버튼이 다 그려질 때까지

# 여기서 준 3초만큼 기다릴건데 그때도 버튼이 안 그려지면  TimeoutException 을 발생시킴
# 그려지면 click()를 해 줘
WebDriverWait(browser, 3).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()

# ----------------------------확인 (+ 버튼이 확장되서 보여지는지)
# Implicity wait
# time.sleep(3)   # 강제로 기다리기(버튼이 나타나도 무조건 기다림)
# browser.find_element_by_xpath('//*[@id="dlMaker_simple"]/dd/div[2]/button[1]').click()


# ----------------------------2번째 방법 확인 (+ 버튼이 확장되서 보여지는지)


# 원하는 모델 카테고리 클릭
# 원하는 제조사의 태그 확인하기

# //*[@id="selectMaker_simple_priceCompare_A"]/li[13]/label

WebDriverWait(browser, 3).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[13]/label'))).click()

# ------------------------- 확인(apple 클릭 되는지)

# print('After Page Contents : {}'.format(browser.page_source))

# ----------------------- 확인

time.sleep(2)    # 약간 대기 시간 주기(빨리 진행 시 에러발생 가능)

soup = BeautifulSoup(browser.page_source, 'html.parser')
# print(soup.prettify())

# ------------------------ 확인

pro_list = soup.select("div.main_prodlist.main_prodlist_list > ul > li")
# print(pro_list)  => selenium WebElement 로 나옴

# -----------------------  메인 상품 페이지 출력

for v in pro_list:
    # 광고 부분에 대해 제거하고 원하는 부분 출력
    # [0]을 안하면 리스트 구조로 가져오기 때문에 해준 것임
    if not v.find('div', class_="ad_header"):
        # 상품명
        print()
        print(v.select('p.prod_name > a')[0].text.strip())

        # 이미지 => data-original 이 있는 경우와 없는 경우가 있으며,
        # src 로 이용할 때도 주소 부분이 다르게 들어 있음
        img = v.select("a.thumb_link > img")[0]
        if img.get('data-original'):
            print(img['data-original'])
        else:
            print(img['src'])

        # 만일 모두 data-original 이 있다면 아래 한줄로 가능
        # print(v.select("a.thumb_link > img")[0]['data-original'])

        # 가격
        print(v.select('p.price_sect > a')[0].text.strip())
    print()

# 브라우저 종료
browser.close()
