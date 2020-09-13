# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    # 스파이더 명
    name = 'test3'

    def start_requests(self):
        yield scrapy.Request('https://blog.scrapinghub.com', self.parse)
        yield scrapy.Request('https://www.naver.com', self.parse)
        yield scrapy.Request('https://www.daum.net', self.parse)

    def parse(self, response):
        # 로그로 확인하기
        self.logger.info("Response URL : {}".format(response.url))
        self.logger.info("Response Status : {}".format(response.status))

        if response.url.find('scrapinghub'):
            yield{
                'sitemap': response.url,
                'contents': response.text[:1000]
            }
        elif response.url.find('naver'):
            yield{
                'sitemap': response.url,
                'contents': response.text[:1000]
            }
        else:
            yield{
                'sitemap': response.url,
                'contents': response.text[:1000]
            }
