# selenium + BeautifulSoup + excel 파일저장
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# wait을 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 마우스나 키보드를 조작하는 모듈
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# 파싱을 위한 모듈
from bs4 import BeautifulSoup

# excel 저장
import openpyxl

# 이미지 요청
import requests

# 가짜 브라우저
from fake_useragent import UserAgent

# 이미지 바이트 처리
from io import BytesIO

import time

# 엑셀 저장과 관련된 코드
workbook = openpyxl.Workbook()
# 기본 워크시트 활성화
worksheet = workbook.active

# 각 열 너비 조정
worksheet.column_dimensions["A"].width = 50
worksheet.column_dimensions["B"].width = 18
worksheet.column_dimensions["C"].width = 10

# 필드명 지정
worksheet.append(["제품명", "가격", "이미지"])


driver = webdriver.Chrome("./driver/chromedriver")
driver.implicitly_wait(3)  # time.sleep(3)
driver.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")

# 확인
# print(driver.page_source)

# 제조사별 더보기 클릭
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='dlMaker_simple']/dd/div[2]/button[1]")
    )
).click()

# 원하는 제조사 클릭 - 애플
# //*[@id="selectMaker_simple_priceCompare_A"]/li[14]/label
WebDriverWait(driver, 3).until(
    EC.presence_of_element_located(
        (By.XPATH, "//*[@id='selectMaker_simple_priceCompare_A']/li[14]/label")
    )
).click()

time.sleep(5)

img_src, idx = "", 1

# 현재 페이지, 크롤링할 페이지 수
cur_page, target_crawl_num = 1, 6

try:
    while cur_page <= target_crawl_num:
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # print(soup.prettify())

        product_list = soup.select("div.main_prodlist > ul > li:not(.product-pot)")
        # print(product_list)

        print("****** 현재 크롤링 페이지 : {}".format(cur_page))

        for product in product_list:
            # 상품명 출력
            if not product.find("div", class_="ad_header"):
                prod_name = product.select_one("p.prod_name > a").text.strip()
                prod_price = product.select_one("p.price_sect > a").text.strip()
                img = product.select_one(".thumb_image img")
                if img.get("data-original"):
                    img_src = img.get("data-original")
                else:
                    img_src = img.get("src")

                # image 주소를 가지고 요청 들어가기
                res = requests.get(
                    "http:" + img_src, headers={"user-agent": UserAgent().chrome}
                )
                prod_img = BytesIO(res.content)

                # print(idx, prod_name, prod_price, "http:" + img_src)
                worksheet.append([prod_name, prod_price])

                # 이미지 저장
                img_save = openpyxl.drawing.image.Image(prod_img)
                img_save.width = 30
                img_save.height = 20
                idx += 1
                worksheet.add_image(img_save, "C" + str(idx))

        # 엑셀 저장
        workbook.save("./crawl/data/danawa_apple.xlsx")

        # 현재 페이지 번호 변경
        cur_page += 1

        # 다음 페이지 번호 클릭하기
        WebDriverWait(driver, 2).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.number_wrap > a:nth-child({})".format(cur_page))
            )
        ).click()

        # soup 인스턴스 삭제
        del soup
        # 다음 페이지 요소들이 보여지는 시간 주기
        time.sleep(3)
except TimeoutException:
    print("**** 종료 *****")

time.sleep(3)
