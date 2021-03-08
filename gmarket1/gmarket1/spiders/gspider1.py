# -*- coding: utf-8 -*-
import scrapy


class Gspider1Spider(scrapy.Spider):
    name = 'gspider1'
    allowed_domains = ['corners.gmarket.co.kr/Bestsellers']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers']

    def parse(self, response):
        print("response.url : {}".format(response.url))

        # 베스트 상품 타이틀 가져오기(플러스 상품까지 포함되서 가져옴)
        # titles = response.css("div.best-list ul li a::text").getall()
        titles = response.css(
            "div.best-list ul:not(.plus) li a::text").getall()

        for idx, title in enumerate(titles, 1):
            print("{}. {}".format(idx, title))
