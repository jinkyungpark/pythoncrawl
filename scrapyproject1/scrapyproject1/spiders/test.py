import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["scrapinghub.com"]
    start_urls = ["http://scrapinghub.com/"]

    def parse(self, response):
        print(response.text)
