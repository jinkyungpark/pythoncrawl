# -*- coding: utf-8 -*-
import scrapy


class SchoolspiderSpider(scrapy.Spider):
    # 스파이더 명
    name = 'schoolspider'
    # 허용 도메인
    allowed_domains = ['w3schools.com']
    # 시작 URL
    start_urls = ['http://w3schools.com/']

    def parse(self, response):

        # getall()

        # menu_lists = response.css(
        #     "nav#mySidenav > div a::text").getall()
        # menu_lists = response.xpath(
        #     "//nav[@id='mySidenav']/div/a/text()").getall()

        # extract()
        # menu_lists = response.css(
        #     "nav#mySidenav > div a::text").extract()
        menu_lists = response.xpath(
            "//nav[@id='mySidenav']/div/a/text()").extract()
        for i, title in enumerate(menu_lists, 1):
            # print("{} : {}".format(i, title))
            yield {
                "no": i,
                "title": title
            }
