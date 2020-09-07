# -*- coding: utf-8 -*-
import scrapy
from gmarket2.items import Gmarket2Item


class Gspider1Spider(scrapy.Spider):
    name = 'gspider1'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers']

    def parse(self, response):
        print("response.url : {}".format(response.url))

        # 베스트 상품 타이틀 가져오기(플러스 상품까지 포함되서 가져옴)
        # titles = response.css("div.best-list ul li a::text").getall()
        titles = response.css(
            "div.best-list ul[class!='plus'] li a::text").getall()
        prices = response.css(
            "div.item_price div.s-price strong span::text").getall()

        for idx, title in enumerate(titles, 0):
            items = Gmarket2Item()
            items['title'] = title
            items['price'] = prices[idx]
            yield items
