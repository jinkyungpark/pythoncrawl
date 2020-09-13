# -*- coding: utf-8 -*-
import scrapy
from naveropenapi.items import NaveropenapiItem
import json


# query : 검색을 원하는 문자열
# display : 검색결과 출력건수 지정(기본:10, 최대 : 100)
# start : 검색 시작 위치로 최대 1000까지 가능(기본 1, 최대 : 1000)
# sort : 정렬옵션

# 주소 만들기(sort는 안주면  유사도순이 기본갑)
# https://openapi.naver.com/v1/search/shop.json?query=샤오미&display=100&start=1


class NavershoppingSpider(scrapy.Spider):
    name = 'navershopping2'
    # allowed_domains = ['openapi.naver.com/v1/search/shop.json?query=']
    start_urls = ['https://openapi.naver.com/v1/search/shop.json?query=']

    def start_requests(self):
        client_id = '6_FpNFqYVz7PeiPV7Omd'
        client_secret = 'S7f9ozjfRZ'
        header_params = {
            "X-Naver-Client-Id": client_id,
            "X-Naver-Client-Secret": client_secret
        }
        query = 'iphone'
        for url in self.start_urls:
            for index in range(10):
                yield scrapy.http.Request(url+query+"&display=100&start="+str(index*100+1), headers=header_params)

    def parse(self, response):
        print(response.text)
        # 넘어오는 데이터 자체가 이미 json 형태이기 때문에 이렇게 처리햐애 함
        data = json.loads(response.body_as_unicode())

        for item in data['items']:
            open_item = NaveropenapiItem()
            open_item['title'] = item['title']
            open_item['link'] = item['link']
            open_item['image'] = item['image']
            open_item['lprice'] = item['lprice']
            open_item['hprice'] = item['hprice']
            open_item['mallName'] = item['mallName']
            open_item['productId'] = item['productId']
            open_item['productType'] = item['productType']
            yield open_item
