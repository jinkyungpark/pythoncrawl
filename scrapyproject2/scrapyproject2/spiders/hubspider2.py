# -*- coding: utf-8 -*-
import scrapy


class Hubspider2Spider(scrapy.Spider):
    name = 'hubspider2'
    allowed_domains = ['www.zyte.com/blog/']
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        """
            :param : response
            :return : Title
        """
        # CSS Selector 이용 / XPath 이용
        # 하나만 가져오기 : get() / extract_first()
        # 전체 가져오기 : getall() / extract()

        # CSS Selector 를 이용한 타이틀 가져오기(21-03-08)
        # sections = response.css(
        #     "#_posts_grid-98-2233 > div.oxy-posts > div.oxy-post")

        # for item in sections:
        #     title = item.css("div.oxy-post-wrap > div > a::text").get()
        #     date = item.css(
        #         "a > div.oxy-post-image-date-overlay::text").get().strip()
        #     # 화면 출력
        #     # print("title : {}".format(title))
        #     # print("date : {}".format(date))

        #     # 리턴 형태
        #     # return type : Request, Item, Dictionary, None
        #     yield {
        #         "title": title,
        #         "date": date
        #     }

        # xpath 이용하기
        sections = response.xpath("//*[@id='_posts_grid-98-2233']/div[1]/div")

        for item in sections:
            title = item.xpath(
                "div[@class='oxy-post-wrap']/div/a/text()").get()
            date = item.xpath(
                "a/div[@class='oxy-post-image-date-overlay']/text()").get().strip()
            # 화면 출력
            print("title : {}".format(title))
            print("date : {}".format(date))

            # 리턴 형태
            # return type : Request, Item, Dictionary, None
            yield {
                "title": title,
                "date": date
            }
