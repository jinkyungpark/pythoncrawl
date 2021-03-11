import scrapy
from ..items import ComputerworldItem

# 아이템 사용 / 상세페이지


class ComputerSpider(scrapy.Spider):
    name = "computer3"
    # allowed_domains = ["https://www.computerworld.com/news"]
    start_urls = ["https://www.computerworld.com/news/"]

    def parse(self, response):
        # 세부기사 링크 가져오기
        links = response.css("div.post-cont h3 a::attr('href')").getall()

        # url : /article/3608956/android-12-little-touches.html
        # response.urljoin(url) : https://www.computerworld.com/article/3606708/android-11-upgrade-report-card.html
        # 아이템으로 저장할 수 있는 코드 추가
        for url in links:
            yield scrapy.Request(
                response.urljoin(url),
                self.parse_article,
                meta={"url": response.urljoin(url)},
            )

    def parse_article(self, response):
        # print(response.url)
        # 타이틀 가져오기
        # title = response.css("h1::text").get()
        # 이미지 주소 가져오기
        # image = response.css("figure.hero-img > img::attr('data-original')").get()
        # 전체 내용 가져오기
        # content = response.css("#drr-container > p::text").getall()

        item = ComputerworldItem()

        item["title"] = response.css("h1::text").get()
        item["img_url"] = response.css(
            "figure.hero-img > img::attr('data-original')"
        ).get()
        item["content"] = "".join(response.css("#drr-container > p::text").getall())
        item["link"] = response.meta["url"]

        yield item
