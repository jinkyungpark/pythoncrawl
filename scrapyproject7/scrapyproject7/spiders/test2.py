# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    # 스파이더 명
    name = 'test2'

    def start_requests(self):
        yield scrapy.Request('https://blog.scrapinghub.com', self.parse)
        yield scrapy.Request('https://www.naver.com', self.parse)
        yield scrapy.Request('https://www.daum.net', self.parse)

    def parse(self, response):
        print(response.url)
