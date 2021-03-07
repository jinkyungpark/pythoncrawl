# -*- coding: utf-8 -*-
import scrapy


class Zytespider1Spider(scrapy.Spider):
    name = 'zytespider1'
    allowed_domains = ['www.zyte.com/blog']
    start_urls = ['http://www.zyte.com/blog/']

    def parse(self, response):
        pass
