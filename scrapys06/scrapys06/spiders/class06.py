# -*- coding: utf-8 -*-
import scrapy
from ..items import ItArticle

# for url in response.xpath('./div[@class="news-item"]/div/div/a/attr("@href")').extract():


class Class06Spider(scrapy.Spider):
    name = 'class06'
    allowed_domains = ['itnews.com']
    start_urls = ['https://itnews.com/']

    def parse(self, response):
        """
        전체 페이지 -> 상세 페이지로 들어가야 하기 때문에
        :param : response
        :return : Request
        """
        # 상세 내용을 보러 들어가기 위한 주소만 추출해서 다시 호출
        for url in response.css('div.news-item > div.hed > div.title > a::attr(href)').extract():
            yield scrapy.Request(response.urljoin(url), self.parse_article)

    def parse_article(self, response):
        # print('>>>>>>>>', response)
        item = ItArticle()
        item['title'] = response.xpath(
            '//h1[@itemprop="headline"]/text()').get()
        item['img_url'] = response.xpath(
            '//img[@itemprop="contentUrl"]/@data-original').get()  # @src 가 안됨
        item['content'] = ''.join(response.xpath(
            '//div[@itemprop="articleBody"]/p/text()').getall())

        yield item
