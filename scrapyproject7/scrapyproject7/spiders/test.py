# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    # 스파이더 명
    name = 'test'
    # 크롤링이 허용된 도메인들
    allowed_domains = ['www.zyte.com/blog', 'naver.com', 'daum.net']
    # 시작 주소
    start_urls = ['https://www.zyte.com/blog/',
                  'https://www.naver.com', 'https://www.daum.net']

    def parse(self, response):
        pass
