import scrapy
from gmarket.items import GmarketItem


class GspiderSpider(scrapy.Spider):
    name = "gspider"
    allowed_domains = ["corners.gmarket.co.kr/Bestsellers"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers"]

    def parse(self, response):
        # g 마켓의 베스트 상품 타이틀 가져오기
        titles = response.css(
            "div.best-list > ul[class!=plus] > li > a::text"
        ).getall()
        # prices = response.xpath(
        #     "//div[@class='best-list']/ul/li/div[@class='item_price']/div[@class='s-price']/strong/span/span/text()"
        # ).getall()
        prices = response.css(
            "div.best-list > ul > li > div.item_price > div.s-price > strong > span > span::text"
        ).getall()
        # print("titles", len(titles))
        # print("prices", len(prices))
        for num, title in enumerate(titles):
            gmarket = GmarketItem()
            gmarket["title"] = title
            gmarket["price"] = int(
                prices[num].strip().replace("원", "").replace(",", "")
            )
            yield gmarket
