from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

from bs4 import BeautifulSoup

# 엑셀 작업
from openpyxl import Workbook
from openpyxl.drawing.image import Image  # Pillow 라이브러리 설치가 필요함

# 이미지 요청
import requests
from io import BytesIO
from fake_useragent import UserAgent

wb = Workbook()
ws1 = wb.active
ws1.column_dimensions["B"].width = 50
ws1.column_dimensions["C"].width = 18
ws1.append(["번호", "제품명", "가격", "이미지"])


options = webdriver.ChromeOptions()
options.headless = True

driver = webdriver.Chrome("d:\\chromedriver\\chromedriver", options=options)

# driver = webdriver.Chrome("d:\\chromedriver\\chromedriver")

driver.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

driver.implicitly_wait(3)

# 제조사별 더보기 클릭
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (
            By.CSS_SELECTOR,
            "div.spec_opt_view > button.btn_spec_view.btn_view_more",
        )
    )
).click()

# print(driver.page_source)

# 특정 제조사 클릭 = APPLE 클릭
WebDriverWait(driver, 2).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='selectMaker_simple_priceCompare_A']/li[17]/label")
    )
).click()


time.sleep(3)


# Apple 노트북 전체 크롤링
cur_page, target_crawl_num = 1, 6

idx = 1

while cur_page <= target_crawl_num:
    # BeautifulSoup 사용
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 현재 크롤링 페이지 출력
    print("*** 현재 페이지 : {}".format(cur_page))

    prod_list = soup.select(
        ".main_prodlist.main_prodlist_list > ul > li:not(.prod_ad_item):not(.product-pot)"
    )
    # print(prod_list)

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

        ws1.append([idx, prod_name, prod_price])

        idx += 1

        # 추출한 이미지 경로를 가지고 이미지 요청 후 가져오기
        headers = {"user-agent": UserAgent().chrome}
        response = requests.get(prod_img_src, headers=headers)
        img_save = BytesIO(response.content)

        img = Image(img_save)
        img.width = 30
        img.height = 20
        ws1.add_image(img, "D" + str(idx))

    wb.save("./danawa.xlsx")

    # 크롤링 페이지 지정
    cur_page += 1

    if cur_page > target_crawl_num:
        print("크롤링 성공")
        break

    # 다음 페이지 번호 클릭
    WebDriverWait(driver, 2).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".number_wrap > a:nth-child({})".format(cur_page))
        )
    ).click()

    # 사용했던 soup 객체 제거
    del soup

    # 페이지 번호 클릭 후 제품이 보여질 때까지 잠시 기다리기
    time.sleep(3)


time.sleep(3)

driver.close()
