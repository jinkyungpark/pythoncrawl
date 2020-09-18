# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GmarketbestItem(scrapy.Item):
    main_cate_name = scrapy.Field()  # main category name
    sub_cate_name = scrapy.Field()   # sub category name
    ranking = scrapy.Field()
    item_code = scrapy.Field()
    title = scrapy.Field()
    ori_price = scrapy.Field()
    dis_price = scrapy.Field()
    discount_percent = scrapy.Field()
