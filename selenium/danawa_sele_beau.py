from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait  # wait 필요
from selenium.webdriver.support import expected_conditions as EC  # 특정조건 지정시 필요
from selenium.webdriver.common.by import By  # 조건 설정
from selenium.common.exceptions import TimeoutException  # WebDriverWait 이 안되면 발생

import time

from bs4 import BeautifulSoup


# 셀레니움+beautiful을 이용하여 애플 첫번째 페이지 제품 가져오기

options = webdriver.ChromeOptions()
options.headless = True

# driver = webdriver.Chrome("d:\\chromedriver\\chromedriver", options=options)
driver = webdriver.Chrome("d:\\chromedriver\\chromedriver")

driver.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

# print(driver.page_source)

try:
    # 새로고침 후 페이지가 다 로드되는 시간만큼 명시적으로 기다리기
    # WebDriver가 기다릴거야 브라우저가 3초간
    # 사용자가 선택하려고 하는 버튼이 다 그려질 때까지

    # 여기서 준 3초만큼 기다릴건데 그때도 버튼이 안 그려지면  TimeoutException 을 발생시킴
    # 그려지면 click()를 해 줘
    # 제조사별 더보기 클릭
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.spec_opt_view > button.btn_spec_view.btn_view_more")
        )
    ).click()

    # 특정 제조사 클릭 = APPLE 클릭
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[@id='selectMaker_simple_priceCompare_A']/li[17]/label")
        )
    ).click()

    time.sleep(3)  # 꼭 필요

    soup = BeautifulSoup(driver.page_source, "html.parser")

    prod_list = soup.select(
        ".main_prodlist.main_prodlist_list > ul > li:not(.prod_ad_item):not(.product-pot)",
    )
    # print(prod_list)

    # 뒤에 여러 페이지를 크롤링 하면서 번호를 붙여나가야 하기 때문에 enumerate() 사용 안함
    idx = 1

    for product in prod_list:
        # 제품명
        prod_name = product.select_one(".prod_name > a").text.strip()
        # 가격
        prod_price = product.select_one(".price_sect > a").text.strip()
        # 이미지 주소
        img = product.select_one(".thumb_image img")
        if img.get("data-original"):
            prod_img_src = img.get("data-original")
        else:
            prod_img_src = img.get("src")

        if "http:" not in prod_img_src:
            prod_img_src = "http:" + prod_img_src

        print(idx, prod_name, prod_price, prod_img_src)

        idx += 1

except TimeoutException as e:
    print(e)


time.sleep(3)

driver.close()
