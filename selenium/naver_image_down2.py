# 2021년 네이버 이미지 다운로드 셀레니움 사용
# requests/fake_useragent/Beautifulsoup

from selenium import webdriver
from selenium.webdriver.common.by import By   # wait 시 필요
from selenium.webdriver.support.ui import WebDriverWait  # 브라우저가 다 로딩될 때 기다려줌
# 어떤 상태가 될때까지 기다려주기 위해 필요
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import os
import time
import urllib.request as req


base = 'https://www.naver.com'


try:
    # 웹 드라이버 로드 -- Headless 모드(개발 다 하고 변경)
    driver = webdriver.Chrome("./webdriver/chrome/chromedriver")

    # Request
    driver.get(base)
    # 요청이 가서 응답을 받을 때까지 잠시 기다려줌
    driver.implicitly_wait(3)
    # 브라우저 최대화
    driver.maximize_window()

    # 검색어를 입력하는 요소 찾기
    element = driver.find_element_by_name("query")
    # 검색어 입력
    element.send_keys("트럭")
    # 엔터
    element.send_keys(Keys.RETURN)

    # 검색결과가 보여지는 페이지(통합 이미지 문서...)
    # 이미지 메뉴(이런 방법으로 찾아도 되고)클릭
    driver.find_element(
        By.CSS_SELECTOR, "ul.base > li:nth-child(2) > a").click()

    # 이런 방법으로 찾아도 됨
    # driver.find_element_by_css_selector(
    #     "ul.base > li:nth-child(2) > a").click()

    savePath = "c:\\imagedown\\"
    # 이미지가 바로 보여지는 형태처럼 보이나 이미지 주소만 넘겨 받아 이미지가 뿌려지는 형태임
    # 사진이 들어가는 그리드 영역이 태그로 보여지는 지 확인하고 이미지의 주소를 가져올 수 있음
    img_tiles = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".photo_tile._grid")))

    # 스크롤 이동
    time.sleep(3)
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 강아지,고양이는 이미지가 로드되지 않는 경우가 있었음

    driver.execute_script(
        "window.scrollTo(0,document.body.scrollHeight/2-100)")  # 이정도로 하니 못 가져오는 이미지가 없었음
    driver.implicitly_wait(5)

    # 스크롤이 이동된 후 브라우저에 기록된 이미지(21-03-04 48개임) 영역을 가져온다.
    images = img_tiles.find_elements_by_css_selector(
        "div.tile_item div.thumb > a > img")

    idx = 1
    for image in images:
        print(idx, image.get_attribute('src'))
        fullfileName = os.path.join(savePath, savePath+str(idx)+".png")
        req.urlretrieve(image.get_attribute("src"), fullfileName)
        idx += 1

    time.sleep(3)
except Exception as e:
    print(e)
finally:
    driver.close()
