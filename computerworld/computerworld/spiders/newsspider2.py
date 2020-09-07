# -*- coding: utf-8 -*-
import scrapy
from ..items import ComputerworldItem


class NewsspiderSpider(scrapy.Spider):
    name = 'newsspider2'
    # allowed_domains = ['www.computerworld.com/news']
    start_urls = ['https://www.computerworld.com/news/']

    def parse(self, response):
        """
            전체 페이지 -> 상세 페이지로 들어가기
            :param : response
            :return : Request
        """
        print("------")
        for url in response.css("div.river-well figure a::attr('href')").extract():
            # print(url)
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    # def parse_article(self, response):
    #     print(">>>>>>", response.url)

    #     # 타이틀
    #     title = response.css("h1::text").get()
    #     # 이미지주소
    #     img_src = response.css(
    #         "div.lede-container figure img::attr('data-original')").get()
    #     # 본문내용
    #     contents = response.xpath(
    #         "//div[@itemprop='articleBody']/p/text()").getall()

    #     yield{
    #         "title": title,
    #         "img_src": img_src,
    #         "contents": contents
    #     }

    # item 사용시
    def parse_article(self, response):
        item = ComputerworldItem()
        # 타이틀
        item['title'] = response.css("h1::text").get()
        # 이미지주소
        item['img_url'] = response.css(
            "div.lede-container figure img::attr('data-original')").get()
        # 본문내용
        # item['contents'] = response.xpath(
        #     "//div[@itemprop='articleBody']/p/text()").getall()

        item['contents'] = ''.join(response.xpath(
            "//div[@itemprop='articleBody']/p/text()").getall())

        yield item
