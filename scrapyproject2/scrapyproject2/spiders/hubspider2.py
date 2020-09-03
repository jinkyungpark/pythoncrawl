# -*- coding: utf-8 -*-
import scrapy


class Hubspider2Spider(scrapy.Spider):
    name = 'hubspider2'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['http://blog.scrapinghub.com/']

    def parse(self, response):
        """
            :param : response
            :return : Title
        """
        # CSS Selector 이용 / XPath 이용
        # 하나만 가져오기 : get() / extract_first()
        # 전체 가져오기 : getall() / extract()

        # CSS Selector 를 이용한 타이틀 가져오기
        titles = response.css("div.post-header > h2 > a::text").getall()
        # CSS Selector 를 이용한 날짜 가져오기
        dates = response.css(
            "div.post-header div.byline span.date a::text").getall()
        for idx, title in enumerate(titles, 0):
            # 화면 출력
            # print("title : {}".format(title))
            # print("date : {}".format(dates[idx]))

            # 리턴 형태
            # return type : Request, Item, Dictionary, None
            yield {
                "title": title,
                "date": dates[idx]
            }
