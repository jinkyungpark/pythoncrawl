# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ItArticle(scrapy.Item):
    # 제목
    title = scrapy.Field()
    # 이미지 URL
    img_url = scrapy.Field()
    # 본문 내용
    content = scrapy.Field()
