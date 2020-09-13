import scrapy
from gmarketbest.items import GmarketbestItem


class GspiderSpider(scrapy.Spider):
    name = "category_all2"
    # 없는 편이 더 좋을 수 있음
    # allowed_domains = ["http://corners.gmarket.co.kr/Bestsellers"]
    # start_urls = ["http://http://corners.gmarket.co.kr/Bestsellers/"]

    base_url = "http://corners.gmarket.co.kr/"

    # start_urls 대신으로 사용할 함수
    def start_requests(self):
        yield scrapy.Request(
            url="http://corners.gmarket.co.kr/Bestsellers/",
            callback=self.parse_allcategories,
        )

    def parse_allcategories(self, response):
        print("mainpages")
        # 카테고리 site 주소 추출하기
        category_links = response.css(
            "div.gbest-cate ul.by-group li a::attr(href)"
        ).getall()
        # 카테고리 명 추출
        category_names = response.css(
            "div.gbest-cate ul.by-group li a::text"
        ).getall()

        for index, category_link in enumerate(category_links):
            # meta : 넘겨주어야 할 파라메터
            yield scrapy.Request(
                url="http://corners.gmarket.co.kr" + category_link,
                callback=self.parse_maincategory,
                meta={"maincategory_name": category_names[index]},
            )

    def parse_maincategory(self, response):
        # print(response.url, response.meta["maincategory_name"])

        # 각 카테고리 별 베스트 상품 가져오기
        # best_list가 많아서 해당 대상인 2번째껄 가져와야 함
        best_items = response.css("div.best-list")[1]

        for idx, item in enumerate(best_items.css("ul > li")):
            ranking = idx+1
            title = item.css("a.itemname::text").get()
            ori_price = item.css("div.o-price::text").get()
            dis_price = item.css("div.s-price strong span span::text").get()
            discount_percent = item.css("div.s-price em::text").get()

            # 가격이 둘 다 없는 경우가 있음 - 무료인 경우
            if dis_price == None:
                dis_price = '0'

            if ori_price == None:
                ori_price = dis_price

            # , 와 원 표시 지우기
            ori_price = ori_price.replace("원", "").replace(",", "")
            dis_price = dis_price.replace("원", "").replace(",", "")

            if discount_percent == None:
                discount_percent = '0'
            else:  # 모든 discount 부분에 붙은 %를 떼어내 버리기
                discount_percent = discount_percent.replace("%", "")

            print(response.meta["maincategory_name"], ranking, title,
                  ori_price, dis_price, discount_percent)
