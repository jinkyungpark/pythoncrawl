from selenium import webdriver

from selenium.webdriver.support.ui import WebDriverWait  # wait 필요
from selenium.webdriver.support import expected_conditions as EC  # 특정조건 지정시 필요
from selenium.webdriver.common.by import By  # 조건 설정
from selenium.common.exceptions import TimeoutException  # WebDriverWait 이 안되면 발생

import time

# 셀레니움을 이용하여 애플 첫번째 페이지 제품 가져오기

options = webdriver.ChromeOptions()
options.headless = True

# driver = webdriver.Chrome("d:\\chromedriver\\chromedriver", options=options)
driver = webdriver.Chrome("d:\\chromedriver\\chromedriver")

driver.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

# print(driver.page_source)

try:
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

    prod_list = driver.find_elements(
        By.CSS_SELECTOR,
        ".main_prodlist.main_prodlist_list > ul > li:not(.prod_ad_item):not(.product-pot)",
    )
    # print(prod_list)

    for idx, product in enumerate(prod_list, 1):
        # 제품명
        prod_name = product.find_element(By.CSS_SELECTOR, ".prod_name > a").text.strip()
        # 가격
        prod_price = product.find_element(
            By.CSS_SELECTOR, ".price_sect > a"
        ).text.strip()
        # 이미지 주소
        img = product.find_element(By.CSS_SELECTOR, ".thumb_image img")
        if img.get_attribute("data-original"):
            prod_img_src = img.get_attribute("data-original")
        else:
            prod_img_src = img.get_attribute("src")

        if "http:" not in prod_img_src:
            prod_img_src = "http:" + prod_img_src

        print(idx, prod_name, prod_price, prod_img_src)

except TimeoutException as e:
    print(e)


time.sleep(3)

driver.close()
