import scrapy
from gmarket.items import GmarketItem


class GspiderSpider(scrapy.Spider):
    name = "gspider"
    allowed_domains = ["corners.gmarket.co.kr/Bestsellers"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers"]

    def parse(self, response):
        # g 마켓의 베스트 상품 타이틀 가져오기
        titles = response.css("div.best-list li > a::text").getall()
        for title in titles:
            gmarket = GmarketItem()
            gmarket["title"] = title
            yield gmarket
