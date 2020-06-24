# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


# LinkExtractor : scrapys 내장 클래스
#                  1page 만 지정해주면 나머지는 알아서 크롤링 해주는 클래스


class NewsSpider(CrawlSpider):
    name = 'news'
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
             callback='parse_headline')
    ]

    def parse_headline(self, response):
        # print(response)
        # URL 로깅
        self.logger.info('Response URL : %s' % response.url)

        for m in response.css('ul.list_news2 > li > div'):
            # 헤드라인
            headline = m.css(
                'strong.tit_thumb > a::text').extract_first().strip()
            # 본문 20글자
            contents = m.css('div > span::text').extract_first().strip()
            yield {'headline': headline, 'contents': contents}
