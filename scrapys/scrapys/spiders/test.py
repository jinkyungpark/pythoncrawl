# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['scrapinghub.com']
    start_urls = ['https://scrapinghub.com/']

    def parse(self, response):
        print('dir', dir(response))   # 사용할 수 있는 함수 정보
        print('status', response.status)  # 상태코드
        print('text', response.body)  # body 정보
