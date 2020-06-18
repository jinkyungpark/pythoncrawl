# -*- coding: utf-8 -*-
import scrapy
from ..items import ItArticle

# Scrapy Feed Export  실습
# 출력 형식
# JSON, JSON Lines
# XML, Pickle, Marshal

# 저장 위치
# Local File System - My PC
# FTP - (Server)
# S3 - (AWS) Amazon
# 기본 콘솔

# 방법 2가지
# 1. 커맨드 이용
# (--output, -o), (--output-format, -t)
# 옵션 설정 예) --set=FEED_EXPORT_INDENT = 2(두번 탭 키 누른 상태)

# 2. Settings.py 이용
# 자동으로 저장(파일명, 형식, 위치)


class Class07Spider(scrapy.Spider):
    name = 'class07'
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
