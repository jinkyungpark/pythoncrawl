# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ArticleItem


class NewsSpider(CrawlSpider):
    name = 'news2'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규 표현식 사용 추천)
    # page=\d$(한자리 수)
    # page=\d+  연속, follow=True
    rules = [
        # 한자리수 페이지 크롤링을 위해서(2~9)
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'),
             callback='parse_parent')
    ]
    # LinkExtractor : scrapys 내장 클래스
    #                  1page 만 지정해주면 나머지는 알아서 크롤링 해주는 클래스

    # 시작 페이지에 대해서는 안해주는 상황
    def parse_start_url(self, response):
        return self.parse_parent(response)

    def parse_parent(self, response):
        # 부모 URL 로깅
        self.logger.info('Parent Response URL : %s' % response.url)
        for url in response.css('ul.list_news2.list_allnews > li > div'):
            # 세부 기사 주소
            article_url = url.css(
                'strong > a::attr(href)').extract_first().strip()
            # 세번째 인자는 현재 몇 페이지의 기사들인지를 알려주기 위해 사용
            # dont_filter 는 True 로 설정되어야 함
            yield scrapy.Request(article_url, self.parse_child, meta={'parent_url': response.url}, dont_filter=True)

    def parse_child(self, response):
        # 부모, 자식 수신 정보 로깅
        self.logger.info('--------------------------')
        self.logger.info('Response From Parent URL : %s' %
                         response.meta['parent_url'])
        self.logger.info('Child Response URL : %s' % response.url)
        self.logger.info('Child Response Status : %s' % response.status)
        self.logger.info('--------------------------')

        # 헤드라인
        headline = response.css('h3.tit_view::text').extract_first().strip()
        # 본문
        c_list = response.css('div.article_view p::text').extract()
        contents = ''.join(c_list).strip()

        yield ArticleItem(headline=headline, contents=contents,
                          parent_link=response.meta['parent_url'], article_link=response.url)
