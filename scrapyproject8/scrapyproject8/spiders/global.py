# -*- coding: utf-8 -*-
import scrapy
from ..items import Scrapyproject8Item


class GlobalSpider(scrapy.Spider):
    name = 'global'
    allowed_domains = ['globalvoices.org']
    start_urls = ['http://globalvoices.org/']

    # def parse(self, response):
    #     # for i, title in enumerate(response.css('div.post-summary-content > div.post-excerpt-container > h3 > a::text').getall(),1):
    #     for i, title in enumerate(response.xpath('//div[@class="post-summary-content"]/div[@class="post-excerpt-container"]/h3/a/text()').getall(), 1):
    #         # print(i, title)
    #         # 인덱스번호, 헤드라인
    #         yield dict(num=i, headline=title)

    def parse(self, response):
        # for i, title in enumerate(response.css('div.post-summary-content > div.post-excerpt-container > h3 > a::text').getall(),1):
        for i, title in enumerate(response.xpath('//div[@class="post-summary-content"]/div[@class="post-excerpt-container"]/h3/a/text()').getall(), 1):
            # 인덱스번호, 헤드라인
            item = Scrapyproject8Item()
            item['num'] = i
            item['headline'] = title
            yield item
