# seeko 의 mainnews 게시판 주소까지 준 다음에 기사 제목 가져오기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chromedriver = "./webdriver/chrome/chromedriver"
driver = webdriver.Chrome(chromedriver)


driver.get("https://seeko.earlyadopter.co.kr/bbs/board.php?bo_table=mainnews")

# #fboardlist > div.list-board > ul > li:nth-child(1) > div.wr-subject > a > span.wr-icon.wr-hot

# 타이틀 수집하기 - copy xpath 로는 위처럼 나와서 짧게 줄임
titles = driver.find_elements_by_xpath("//div[@class='wr-subject']/a")
# 조회수 수집하기  //*[@id="fboardlist"]/div[1]/ul/li[1]/div[5]
counts = driver.find_elements_by_xpath("//div[@class='wr-hit hidden-xs']")

article_list = list()

for i in range(15):
    article_list.append([titles[i].text, counts[i].text])

# 제목과 조회수 출력
print(article_list)
driver.quit()
