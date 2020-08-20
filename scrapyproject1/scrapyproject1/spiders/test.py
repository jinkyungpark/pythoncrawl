import scrapy


class TestSpider(scrapy.Spider):
    name = "test"
    allowed_domains = ["blog.scrapinghub.com", "gmarket.co.kr"]
    start_urls = [
        "http://blog.scrapinghub.com/",
        "http://www.gmarket.co.kr",
    ]

    def parse(self, response):
        # print(response.text) 이렇게 가지고 오면 보기도 힘들고
        # start_urls가 여러개 있는 경우 어느 url에서 왔는지 확인
        # 뒤에 있는 것부터 크롤링 됨
        print(response.url)
        print("dir", dir(response))  # 사용할 수 있는 함수 정보
        print("status", response.status)  # 상태코드
        print("text", response.body)  # body 정보
