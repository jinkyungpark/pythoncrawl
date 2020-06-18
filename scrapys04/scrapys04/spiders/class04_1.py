# -*- coding: utf-8 -*-
import scrapy


class Class041Spider(scrapy.Spider):
    name = 'class04-1'
    allowed_domains = ['blog.scrapinghub.com', 'naver.com', 'daum.net']
    start_urls = ['http://blog.scrapinghub.com/',
                  'https://www.naver.com', 'https://www.daum.net']

    # settings.py 동적으로 설정하기
    # custom_settings = {
    #     'DOWNLOAD_DELAY': 3
    # }

    # Request 각각 지정하는 방식
    # def start_request(self):
    #     yield scrapy.Request('http://blog.scrapinghub.com',self.parse)
    #     yield scrapy.Request('https://www.naver.com',self.parse)
    #     yield scrapy.Request('https://www.daum.net',self.parse)

    def parse(self, response):
        # 로그 확인
        self.logger.info("Response URL : %s" % response.url)
        self.logger.info("Response Status : %s" % response.status)

        if response.url.find('scrapinghub'):
            yield{
                'sitemap': response.url,
                'contents': response.text[:1000]
            }
        elif response.url.find("naver"):
            yield{
                'sitemap': response.url,
                'contents': response.text[:1000]
            }
        else:
            yield{
                'sitemap': response.url,
                'contents': response.text[:1000]
            }
