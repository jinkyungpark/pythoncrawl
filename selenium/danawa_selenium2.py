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
driver.maximize_window()
driver.get("http://prod.danawa.com/list/?cate=112758")

# print(driver.page_source)

# 제조사별 더보기 클릭
# driver.find_element_by_css_selector("div.spec_opt_view button").click()
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.spec_opt_view button"))
).click()

# apple 클릭
driver.find_element(
    By.CSS_SELECTOR, "#selectMaker_simple_priceCompare_A li:nth-child(17)"
).click()

time.sleep(3)

# 하단의 제품 출력 => 1~6 page

cur_page, target_crawl_num = 1, 6
idx = 1

while cur_page <= target_crawl_num:

    # 전체 상품 목록 가져오기
    prod_list = driver.find_elements(
        By.CSS_SELECTOR,
        ".main_prodlist.main_prodlist_list > ul > li:not(.prod_ad_item):not(.product-pot)",
    )

    # 현재 페이지 출력
    print("***** 현재 페이지 : {}".format(cur_page))

    for product in prod_list:
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

        idx += 1

    # 현재 페이지 번호 변경
    cur_page += 1

    if cur_page > target_crawl_num:
        print("Crawling 성공")
        break

    # 다음 페이지 번호 클릭하기
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.number_wrap > a:nth-child({})".format(cur_page))
        )
    ).click()

    time.sleep(3)

driver.close()
