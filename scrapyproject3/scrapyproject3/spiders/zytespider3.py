# -*- coding: utf-8 -*-
import scrapy


class Zytespider3Spider(scrapy.Spider):
    name = 'zytespider3'
    allowed_domains = ['www.zyte.com']
    start_urls = ['https://www.zyte.com/blog/']

    def parse(self, response):
        """
            param : response
            return : Request
        """

        for url in response.css(
                "#_posts_grid-98-2233 > div.oxy-posts > div.oxy-post > div.oxy-post-wrap > div > a::attr('href')").extract():
            # print(url)
            # 재귀호출 시 상대경로로 되어 있는 주소를 절대 경로로 바꿔주기
            # urljoin 사용
            # print(response.urljoin(url))
            yield scrapy.Request(url=response.urljoin(url), callback=self.parse_article)

    def parse_article(self, response):
        """
        상세페이지 -> 타이틀 추출
        :param : response
        :return Text
        """
        # 현재 url 이 무엇인지 확인
        # print(response.url)

        # [:10] #blog-body
        contents = response.css(
            '#blog-body > span > p::text').extract_first()[:50]
        print(contents)

        # items 사용
        # items = Scrapyproject3Item()
        # items['content'] = ''.join(contents)
        # yield items
