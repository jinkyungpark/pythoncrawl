# -*- coding: utf-8 -*-
import scrapy


class Class021Spider(scrapy.Spider):
    name = 'class02-1'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
            :param : response
            :return : Title Text
        """

        # CSS Selector 이용 /  XPath 이용
        # 하나만 가져오기 : get() / extract_first()
        # 전체 가져오기 : extract() / getall()

        # -------- CSS Selector 이용하기
        # a까지만 적어주면 a 태그 전체를 가져오기 때문에
        # for text in response.css('div.post-header h2 a::text').getall():
        #     # return Type : Request, BaseItem, Dictionary, None
        #     yield {
        #         'title': text
        #     }

        # -------- XPath 이용하기
        for i, text in enumerate(response.xpath('//div[@class="post-header"]/h2/a/text()').getall()):
            yield{
                'number': i,
                'title': text
            }
