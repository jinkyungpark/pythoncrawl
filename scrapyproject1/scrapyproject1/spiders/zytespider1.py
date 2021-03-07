# -*- coding: utf-8 -*-
import scrapy


class Zytespider1Spider(scrapy.Spider):
    name = 'zytespider1'
    allowed_domains = ['www.zyte.com/blog']
    start_urls = ['http://www.zyte.com/blog/']

    def parse(self, response):
        # print(response.text)
        print("response.url : {}".format(response.url))
        print("dir : {}".format(dir(response)))  # 사용할 수 있는 함수 정보
        print("status : {}".format(response.status))  # 상태코드
        print("body : {}".format(response.body))      # body 정보
