# -*- coding: utf-8 -*-
import scrapy


class Class051Spider(scrapy.Spider):
    # 스파이더 이름(실행)
    name = 'class05'
    # 허용 도메인
    allowed_domains = ['w3schools.com']
    # 시작 URL
    start_urls = ['https://www.w3schools.com/']

    def parse(self, response):
        # 둘다 가능
        # response.css("nav#mySidenav > div a::text").getall()
        # response.xpath('//nav[@id="mySidenav"]/div//a/text()').getall()    or extract()
        for i, title in enumerate(response.css("nav#mySidenav > div a::text").getall(), 1):
            yield{
                'num': i,
                'learn title': title
            }
