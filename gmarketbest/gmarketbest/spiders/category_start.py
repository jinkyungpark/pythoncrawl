# 내가 작성한 것 => 아이템 코드까지 포함된 상태
import scrapy
from gmarketbest.items import GmarketbestItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import re


class GspiderSpider(CrawlSpider):
    name = "category_start"

    allowed_domains = ["corners.gmarket.co.kr"]
    start_urls = ["http://corners.gmarket.co.kr/Bestsellers/"]

    rules = [
        Rule(LinkExtractor(allow=r'/Bestsellers\?viewType=G&groupCode=G(0|1)\d$'),
             callback='parse_sub_category')
    ]

    # start_url 페이지는 서브 카테고리는 없기 때문에 바로 best100 추출
    def parse_start_url(self, response):
        print(">>>>> parse_start_url ", response.url)

    # ALL을 제외한 카테고리가 호출하는 부분 - 각 카테고리별 best100 추출 호출 및 2차 카테고리 추출
    def parse_sub_category(self, response):
        print(">>>>> parse_sub_category ", response.url)

    # 1차, 2차 카테고리 주소를 넘겨받아 best 상품 추출하기

    def parse_item(self, response):
        # 어디서 왔는지 확인
        print("parse_item {}, main_cate {}, sub_cate {}".format(response.url,
                                                                response.meta["main_cate_name"], response.meta["sub_cate_name"]))

        # ALL : 1~200 아이템 추출
        # 나머지 : 1~100 아이템 추출
        best_list = response.css("div.best-list")[1]

        # 아이템 전체 가져오기
        best_list_items = best_list.css("ul li")

        # 아이템 추출
        for idx, item in enumerate(best_list_items, 1):

            ranking = idx
            title = item.css("a::text").get()

            # 아이템 코드 추출
            href = item.css("a::attr('href')").get()
            pattern = re.compile("code=[0-9]+")
            item_code = pattern.findall(href)[0].split("=")[1]

            ori_price = item.css(
                "div.item_price div.o-price span span::text").get()
            dis_price = item.css(
                "div.item_price div.s-price strong span span::text").get()
            discount_percent = item.css(
                "div.item_price div.s-price span em::text").get()

            # 후 처리
            # 가격이 둘 다 없는 경우가 있음 - 무료인 경우
            if dis_price == None:
                dis_price = "0"

            if ori_price == None:
                ori_price = dis_price

            # , 와 원 표시 지우기
            ori_price = ori_price.replace("원", "").replace(",", "")
            dis_price = dis_price.replace("원", "").replace(",", "")

            if discount_percent == None:
                discount_percent = '0'
            else:  # 모든 discount 부분에 붙은 %를 떼어내 버리기
                discount_percent = discount_percent.replace("%", "")

            # print(response.meta["main_cate_name"], response.meta["sub_cate_name"], ranking, item_code, title,
            #       ori_price, dis_price, discount_percent)

            best_item = GmarketbestItem()
            best_item['main_cate_name'] = response.meta["main_cate_name"]
            best_item['sub_cate_name'] = response.meta["sub_cate_name"]
            best_item['item_code'] = item_code
            best_item['ranking'] = ranking
            best_item['title'] = title
            best_item['ori_price'] = ori_price
            best_item['dis_price'] = dis_price
            best_item['discount_percent'] = discount_percent
            yield best_item
