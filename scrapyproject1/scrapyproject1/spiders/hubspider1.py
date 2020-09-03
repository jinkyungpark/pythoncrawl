# -*- coding: utf-8 -*-
import scrapy


class Hubspider1Spider(scrapy.Spider):
    name = 'hubspider1'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):
        # print(response.text)
        print("response.url : {}".format(response.url))
        print("dir : {}".format(dir(response)))  # 사용할 수 있는 함수 정보
        print("status : {}".format(response.status))  # 상태코드
        print("body : {}".format(response.body))      # body 정보
