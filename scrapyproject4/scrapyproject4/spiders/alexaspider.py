# -*- coding: utf-8 -*-
import scrapy
from ..items import SiteRankItems


class AlexaspiderSpider(scrapy.Spider):
    name = 'alexaspider'
    allowed_domains = ['alexa.com/topsites']
    start_urls = ['http://alexa.com/topsites/']

    def parse(self, response):
        """
        :param : response
        :return : SiteRankItems
        """
        for p in response.css('div.listings.table > div.tr.site-listing'):
            # print(p)
            item = SiteRankItems()
            item['rank_num'] = p.xpath('div[@class="td"]/text()').get()
            item['site_name'] = p.xpath(

                'div[@class="td DescriptionCell"]/p/a/text()').get()
            item['daily_time_site'] = p.xpath(
                'div[@class="td right"]/p/text()').getall()[0]
            item['daily_page_view'] = p.xpath(
                'div[@class="td right"]/p/text()').getall()[1]
            yield item
