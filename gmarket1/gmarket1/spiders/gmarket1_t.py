from scrapy_selenium import SeleniumRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import scrapy


class Gmarket1Spider(scrapy.Spider):
    name = "gmarket1_t"
    # allowed_domains = ["corners.gmarket.co.kr"]
    start_urls = [
        "http://corners.gmarket.co.kr/Bestsellers?viewType=G&groupCode=G11"]

    def parse(self, response):
        urls = response.css(
            "#gBestWrap > div > div:nth-child(5) > div:nth-child(3) > ul > li > a::attr('href')"
        ).getall()

        for url in urls:
            # print("url : {}".format(url))
            yield SeleniumRequest(url=url, callback=self.parse_url, wait_time=3, wait_until=EC.element_to_be_clickable((By.CSS_SELECTOR, 'h1.itemtit')))

    def parse_url(self, response):
        # print("parse_url : {}".format(response.url))
        # 상품명
        title = response.css("h1::text").get()
        # title = response.xpath('//*[@id="itemcase_basic"]/div[1]/h1/text()')
        # print("여행 상품명 : {}".format(title))
        yield{
            "상품 url": response.url,
            "여행상품명": title
        }
