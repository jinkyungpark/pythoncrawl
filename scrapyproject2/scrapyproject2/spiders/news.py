# -*- coding: utf-8 -*-
import scrapy
from ..items import ArticleItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# LinkExtractor : scrapys 내장 클래스
#                  1page 만 지정해주면 나머지는 알아서 크롤링 해주는 클래스


class NewsSpider(CrawlSpider):
    name = 'news2'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규 표현식 사용 추천)
    # page=\d$(한자리 수)
    # page=\d+  연속, follow=True
    rules = [
        # \d$ 로 끝났으니 1~9까지만 크롤링
        # Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d+'),
        #      callback='parse_headline', follow=True)

        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'),
             callback='parse_parent')
    ]

    # 시작 페이지에 대해서는 안해주는 상황임
    def parse_start_url(self, response):
        return self.parse_parent(response)

    def parse_parent(self, response):
        # print(response)
        # 부모 URL 로깅
        self.logger.info('Parent Response URL : %s' % response.url)
        for url in response.css('ul.list_news2.list_allnews > li > div'):
            # 세부 기사 주소
            article_url = url.css(
                'strong.tit_thumb > a::attr(href)').extract_first().strip()
            self.logger.info("article_url : %s " % article_url)
            # 세번째 인자는 현재 몇 페이지의 기사들인지를 알려주기 위해 사용
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url': response.url})

    def parse_child(self, response):
        print("apdfeeef")
        # 부모, 자식 수신 정보 로깅
        self.logger.info('--------------------------')
        self.logger.info('Response From Parent URL : %s' %
                         response.meta['parent_url'])
        self.logger.info('Child Response URL : %s' % response.url)
        self.logger.info('Child Response Status : %s' % response.status)
        self.logger.info('--------------------------')
