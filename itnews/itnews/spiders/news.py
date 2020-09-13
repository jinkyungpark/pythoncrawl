# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['news.daum.net']
    start_urls = ['https://news.daum.net/breakingnews/digital']

    # 링크 크롤링 규칙(정규 표현식 사용 추천)
    # page=\d$(한자리 수)
    # page=\d+  연속, follow=True
    rules = [
        # 한자리 수 ~ 여러 자리수 이상의 페이지 크롤링
        # Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d+'),
        #      callback='parse_headline', follow=True)

        # # 한자리수 페이지 크롤링을 위해서(2~9)
        Rule(LinkExtractor(allow=r'/breakingnews/digital\?page=\d$'),
             callback='parse_headline')
    ]
    # LinkExtractor : scrapys 내장 클래스
    #                  1page 만 지정해주면 나머지는 알아서 크롤링 해주는 클래스

    # 시작 페이지에 대해서는 안해주는 상황
    def parse_start_url(self, response):
        return self.parse_headline(response)

    def parse_headline(self, response):
        self.logger.info("response url {}".format(response.url))

        for m in response.css('ul.list_news2.list_allnews > li > div'):
            # 헤드라인
            headline = m.css(
                'strong > a::text').extract_first().strip()
            # 본문 20글자
            contents = m.css('div > span::text').extract_first().strip()
            yield {'headline': headline, 'contents': contents}
