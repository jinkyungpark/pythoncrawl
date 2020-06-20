# -*- coding: utf-8 -*-
import scrapy
from ..items import GlobalTitle


class Class08Spider(scrapy.Spider):
    name = 'class08'
    allowed_domains = ['globalvoices.org']
    start_urls = ['https://globalvoices.org/']


    custom_settings = {
        'DOWNLOAD_DELAY' : 3
    }


    # def parse(self, response):
    #    # for i, title in enumerate(response.css('div.post-summary-content > div.post-excerpt-container > h3 > a::text').getall(),1):
    #    for i, title in enumerate(response.xpath('//div[@class="post-summary-content"]/div[@class="post-excerpt-container"]/h3/a/text()').getall(),1):
    #         # print(i, title)
    #         # 인덱스번호, 헤드라인
    #         yield dict(num=i, headline=title)


    def parse(self, response):
       # for i, title in enumerate(response.css('div.post-summary-content > div.post-excerpt-container > h3 > a::text').getall(),1):
       for i, title in enumerate(response.xpath('//div[@class="post-summary-content"]/div[@class="post-excerpt-container"]/h3/a/text()').getall(),1):
            # 인덱스번호, 헤드라인
            item = GlobalTitle()
            item['num'] = i
            item['headline'] = title
            yield item