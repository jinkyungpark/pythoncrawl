# -*- coding: utf-8 -*-
import scrapy
from ..items import Scrapyproject3Item


class Hubspider3Spider(scrapy.Spider):
    name = 'hubspider3'
    allowed_domains = ['blog.scrapinghub.com']
    start_urls = ['https://blog.scrapinghub.com/']

    def parse(self, response):
        """
            param : response
            return : Request
        """
        for url in response.css('div.post-item > div > h2 > a::attr("href")').extract():
            # print(url)
            # 재귀호출 시 상대경로로 되어 있는 주소를 절대 경로로 바꿔주기
            # urljoin 사용
            yield scrapy.Request(response.urljoin(url), self.parse_title)

    def parse_title(self, response):
        """
        상세페이지 -> 타이틀 추출
        :param : response
        :return Text
        """
        contents = response.css(
            'div.post-body > span > p::text').extract()[:10]
        # print(contents)
        # yield{'contents': ''.join(contents)}  # 리스트 형태로 나오기 때문에 텍스트 형식으로 변경

        # items 사용
        items = Scrapyproject3Item()
        items['content'] = ''.join(contents)
        yield items
