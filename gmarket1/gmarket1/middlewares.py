# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy import signals
from scrapy.http import HtmlResponse
from scrapy.utils.python import to_bytes

from selenium.webdriver.common.by import By   # wait 시 필요
from selenium.webdriver.support.ui import WebDriverWait  # 브라우저가 다 로딩될 때 기다려줌
# 어떤 상태가 될때까지 기다려주기 위해 필요
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


class SeleniumMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        middleware = cls()
        crawler.signals.connect(middleware.spider_opened,
                                signal=signals.spider_opened)
        crawler.signals.connect(middleware.spider_closed,
                                signal=signals.spider_opened)
        return middleware

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

        driver = webdriver.Chrome(
            "D:\\pythoncrawl\\webdriver\\chrome\\chromedriver.exe")
        self.driver = driver

    def spider_closed(self, spider):
        spider.logger.info('Spider closed: %s' % spider.name)

        self.driver.close()

    def process_request(self, request, spider):
        self.driver.get(request.url)

        time.sleep(2)
        # WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
        #     (By.CSS_SELECTOR, "h1.itemtit")))
        body = to_bytes(text=self.driver.page_source)

        time.sleep(3)

        return HtmlResponse(url=request.url, body=body, encoding='utf-8', request=request)
