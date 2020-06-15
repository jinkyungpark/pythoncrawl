# danawa2 다른 이름으로 저장
# 크롤링 된 정보를 엑셀로 저장하기

from selenium import webdriver
import time
from selenium.webdriver.common.by import By   # wait 시 필요
from selenium.webdriver.support.ui import WebDriverWait  # 브라우저가 다 로딩될 때 기다려줌
# 어떤 상태가 될때까지 기다려주기 위해 필요
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# 엑셀 처리 임포트
import xlsxwriter
# 이미지 바이트 처리
from io import BytesIO
# 저장
import urllib.request as req


# 엑셀 처리 선언
workbook = xlsxwriter.Workbook("c:/crawling_result.xlsx")
# 워크 시트 작성
worksheet = workbook.add_worksheet()


# 크롬 브라우저 옵션 설정
chrome_options = Options()
# 이전까지 브라우저가 실행됐다가 꺼지는 상태였기 때문에 안하기 위해
chrome_options.add_argument("--headless")

# 웹 드라이버 로드 -- Headless 모드(개발 다 하고 변경)
browser = webdriver.Chrome(
    "./webdriver/chrome/chromedriver.exe", options=chrome_options)

# -------------------------- 확인(브라우저가 안 뜨는지 확인 : 일반모드)

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


WebDriverWait(browser, 3).until(EC.presence_of_element_located(
    (By.XPATH, '//*[@id="selectMaker_simple_priceCompare_A"]/li[13]/label'))).click()

time.sleep(2)    # 약간 대기 시간 주기(빨리 진행 시 에러발생 가능)

# ------------------------------------------ 페이지 나누기

# 현재 페이지
cur_page = 1

# 크롤링할 페이지 수
taget_crawl_num = 7

# 엑셀 행 수
ins_cnt = 1


while cur_page <= taget_crawl_num:

    soup = BeautifulSoup(browser.page_source, 'html.parser')
    # print(soup.prettify())

    # ------------------------ 확인

    pro_list = soup.select("div.main_prodlist.main_prodlist_list > ul > li")
    # print(pro_list)

    # 현재 페이지 출력
    print("**** Current Page : {}".format(cur_page))

    # -----------------------  메인 상품 페이지 출력

    for v in pro_list:
        # 광고 부분에 대해 제거하고 원하는 부분 출력
        # [0]을 안하면 리스트 구조로 가져오기 때문에 해준 것임
        if not v.find('div', class_="ad_header"):
            # 상품명
            prod_name = v.select('p.prod_name > a')[0].text.strip()

            # 이미지
            img = v.select("a.thumb_link > img")[0]
            if img.get('data-original'):
                url = img['data-original']
            else:
                url = img['src']

            # print("img 경로 : {}".format(url))

            # 403에러 때문에 수정
            # prod_img = BytesIO(req.urlopen(url).read())

            request = req.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            prod_img = BytesIO(req.urlopen(request).read())  # 이미지 요청 후 Byte 변환

            # 가격
            prod_price = v.select('p.price_sect > a')[0].text.strip()

            # 엑셀 파일 저장
            # A1 셀부터 입력될 것이기 때문에
            worksheet.write('A%s' % ins_cnt, prod_name)
            worksheet.write('B%s' % ins_cnt, prod_price)

            # 엑셀 저장 이미지(형식은 지정되어 있는 것=> 딕셔너리)
            # x_scale, y_scale 를 줘서 축소시킬 수도 있음
            # worksheet.insert_image('C%s' % ins_cnt, prod_name, {
            #                        'image_data': prod_img, 'x_scale': 0.3, 'y_scale': 0.3})
            worksheet.insert_image('C%s' % ins_cnt, prod_name, {
                                   'image_data': prod_img})
            ins_cnt += 1

        print()

    # 페이지 별 스크린 샷 저장
    # browser.save_screenshot('c:/target_page{}.png'.format(cur_page))

    # 현재 페이지 번호 변경
    cur_page += 1

    if(cur_page > taget_crawl_num):
        print("Crawling 성공")
        break

    # 다음 페이지 번호 클릭하는 부분(XPATH 로는 에러남)
    WebDriverWait(browser, 2).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, 'div.number_wrap > a:nth-child({})'.format(cur_page)))).click()

    # BeautifulSoup 인스턴스 삭제
    del soup

    # 3초간 대기
    time.sleep(3)
# 브라우저 종료
browser.close()

# 엑셀 스트림 종료(반드시 필요)
workbook.close()
