# -*- coding: utf-8 -*-
import scrapy


class NewsspiderSpider(scrapy.Spider):
    name = 'newsspider'
    allowed_domains = ['www.computerworld.com/news/']
    start_urls = ['http://www.computerworld.com/news//']

    def parse(self, response):
        print(response.url)

        # 세부 기사 링크 가져오기
        article_links = response.css(
            "div.river-well figure a::attr('href')").getall()
        # 이미지 전체 주소 가져오기(src 가 있는 것으로 보여지지만 실제로느 없음)
        article_images = response.css(
            "div.river-well > figure > a > img::attr('data-original')").getall()
        # 타이틀 모두 가져오기
        article_titles = response.css(
            "div.river-well div.post-cont h3 a::text").getall()
        # 내용 모두 가져오기
        article_contents = response.css(
            "div.river-well div.post-cont h4::text").getall()
        for i, article in enumerate(article_titles, 0):
            # 세부 기사 링크
            link = article_links[i]
            # 제목
            title = article
            # 이미지 url
            img_url = article_images[i]
            # 내용
            contents = article_contents[i]

            yield{
                'title': title,
                'link': link,
                'url': img_url,
                'contents': contents
            }
