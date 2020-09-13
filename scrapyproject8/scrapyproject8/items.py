# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Scrapyproject8Item(scrapy.Item):
    # 번호
    num = scrapy.Field()
    # 타이틀
    headline = scrapy.Field()
