import pymysql
import datetime
from scrapy.exceptions import DropItem


class ItnewsPipeline:
    # 초기화 메소드
    def __init__(self):
        # mysql connect
        self.conn = pymysql.Connect(host="localhost", port=3306, user="root",
                                    passwd="12345", db="ecommerce", charset="utf8")
        if self.conn:
            print("Connection 성공")
        else:
            print("Connection 실패")

        self.cursor = self.conn.cursor()

    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info("NewsSpider Pipeline Started.")
        sql = """
                CREATE TABLE IF NOT EXISTS NEWS_DATA(id int PRIMARY KEY AUTO_INCREMENT,
                HEADLINE varchar(100), contents varchar(5000), parent_link varchar(100),
                article_link varchar(100), crawled_time varchar(50))
        """

        self.cursor.execute(sql)

    # Item 건수별 실행

    def process_item(self, item, spider):
        if not item.get('contents') is None:
            # 크롤링 시간 필드 추가
            item['crawled_time'] = datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S')
            # 데이터 삽입
            sql = """
                INSERT INTO NEWS_DATA(HEADLINE, CONTENTS, PARENT_LINK,ARTICLE_LINK,CRAWLED_TIME)
                VALUES(%s,%s,%s,%s,%s);
            """
            values = (item.get('headline'), item.get('contents'), item.get(
                'parent_link'), item.get("article_link"), item.get("crawled_time"))

            self.cursor.execute(sql, values)
            self.conn.commit()

            spider.logger.info("Item DB inserted")
            return item
        else:
            raise DropItem("Dropped Item.")

    # 마지막 1회 실행
    def close_spider(self, spider):
        spider.logger.info("NewsSpider Pipeline Stopped.")
        self.conn.close()
