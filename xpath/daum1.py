from selenium import webdriver
from selenium.webdriver.common.keys import Keys


chromedriver = "d:/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(chromedriver)

driver.get("https://news.v.daum.net/v/20200817153136659")
# //*[@id="cSub"]/div/h3
print(driver.find_element_by_xpath("//*[@id='cSub']/div/h3").text)
# <title> 태그 안의 값 가져오기를 xpath로 하는 경우
print(driver.find_element_by_xpath("//title").get_attribute("text"))

driver.quit()
