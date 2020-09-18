# 동강2 - items 사용 후
import scrapy
from gmarketbest.items import GmarketbestItem


class GspiderSpider(scrapy.Spider):
    name = "category_all3"
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

        # 첫번째 카테고리에서 best 상품 추출을 위한 코드
        # 1차 카테고리의 best100 개를 추출할때는 subcategory가 모두 없는 상태이기 때문에
        # 임의로 ALL 로 만들어 넘겨줌
        for index, category_link in enumerate(category_links):
            # meta : 넘겨주어야 할 파라메터
            yield scrapy.Request(
                url="http://corners.gmarket.co.kr" + category_link,
                callback=self.parse_maincategory,
                meta={
                    "maincategory_name": category_names[index], "subcategory_name": "ALL"},
            )

        # 각 서브 카테고리에서 2차 서브 카테고리 상품 추출을 위한 코드
        for index, category_link in enumerate(category_links):
            # meta : 넘겨주어야 할 파라메터
            yield scrapy.Request(
                url="http://corners.gmarket.co.kr" + category_link,
                callback=self.parse_subcategory,
                meta={"maincategory_name": category_names[index]}, dont_filter=True
            )

    def parse_maincategory(self, response):
        print(response.url,
              response.meta["maincategory_name"], response.meta["subcategory_name"])

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

            # print(response.meta["maincategory_name"], ranking, title,
            #       ori_price, dis_price, discount_percent)

            item = GmarketbestItem()
            item['main_cate_name'] = response.meta["maincategory_name"]
            item['sub_cate_name'] = response.meta["subcategory_name"]
            item['ranking'] = ranking
            item['title'] = title
            item['ori_price'] = ori_price
            item['dis_price'] = dis_price
            item['discount_percent'] = discount_percent
            yield item

    def parse_subcategory(self, response):
        # print("parse_subcategory", response.meta["maincategory_name"])

        maincategory_name = response.meta["maincategory_name"]

        # 2차 카테고리 추출 - 컴퓨터/전자 - 관련상품군(하이마트 안 나오도록 만들어야 함)
        subcategory_links = response.css(
            "div.navi ul li[class!='related'] a::attr('href')").getall()
        subcategory_names = response.css(
            "div.navi ul li[class!='related'] a::text").getall()
        for index, category_link in enumerate(subcategory_links):
            # print(maincategory_name, response.meta["maincategory_name"],
            #       subcategory_names[index], category_link)
            yield scrapy.Request(
                url="http://corners.gmarket.co.kr" + category_link,
                callback=self.parse_maincategory,
                meta={
                    "maincategory_name": maincategory_name, "subcategory_name": subcategory_names[index]},
            )
