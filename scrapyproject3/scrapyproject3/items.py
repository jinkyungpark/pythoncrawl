# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticleItem(scrapy.Item):

    # 요청 리스트 페이지
    parent_link = scrapy.Field()
    # 기사제목
    headline = scrapy.Field()
    # 해당 기사 URL
    article_link = scrapy.Field()
    # 기사 본문
    contents = scrapy.Field()
    # 수집된 시간
    crawled_time = scrapy.Field()
