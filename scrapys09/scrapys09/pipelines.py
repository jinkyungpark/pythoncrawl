# 잘못된 데이터 제거, DB 저장, SMS 전송, 메일 전송, SNS 전송
from scrapy.exceptions import DropItem


class Scrapys09Pipeline(object):
    # 최초 한 번만 실행
    def open_spider(self, spider):
        spider.logger.info('Scrapys09Pipeline Started.')

    # item : Item으로 작성한 것들이 하나하나 통과하게 되는 것

    def process_item(self, item, spider):
        if int(item.get('rank_num')) < 11:
            item['is_pass'] = True
            return item
        else:
            raise DropItem(
                f'Dropped Item. Because This Site Rank is {item.get("rank_num")}')

    # 마지막 1회 실행
    def close_spider(self, spider):
        spider.logger.info('Scrapys09Pipeline Closed.')
