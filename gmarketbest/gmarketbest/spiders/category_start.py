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
        # print(">>>>> parse_start_url ", response.url)
        yield scrapy.Request(url=response.)

    # ALL을 제외한 카테고리가 호출하는 부분 - 각 카테고리별 best100 추출 호출 및 2차 카테고리 추출
    def parse_sub_category(self, response):
        print(">>>>> parse_sub_category ", response.url)

    # 1차, 2차 카테고리 주소를 넘겨받아 best 상품 추출하기
    def parse_item(self, response):
        # 어디서 왔는지 확인
        print("parse_item {}, main_cate {}, sub_cate {}".format(response.url,
                                                                response.meta["main_cate_name"], response.meta["sub_cate_name"]))

        best_list = response.css("div.best-list")[1]
