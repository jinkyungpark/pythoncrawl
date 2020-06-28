import datetime
import sqlite3

from scrapy.exceptions import DropItem


class NewsSpiderPipeline(object):

    # 초기화 메소드
    def __init__(self):
        # pass
        # isolation_level = None(auto commit)
        self.conn = sqlite3.connect('c:/database_db.db', isolation_level=None)
        # DB 연결
        self.c = self.conn.cursor()

    # 최초 1회 실행
    def open_spider(self, spider):
        spider.logger.info('NewSpider Pipeline Started.')
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS NEWS_DATA(id INTEGER PRIMARY KEY AUTOINCREMENT," +
            "headline text, contents text, parent_link text, article_link text,crawled_time text)")

    # Item 건수 별 실행
    def process_item(self, item, spider):
        if not item.get('contents') is None:
            # 크롤링 시간 필드 추가
            item['crawled_time'] = datetime.datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S')
            # 데이터 -> DB 삽입
            self.c.execute(
                'INSERT INTO NEWS_DATA(headline,contents,parent_link,article_link,crawled_time)' +
                'values(?,?,?,?,?);', (item.get('headline'), item.get('contents'),
                                       item.get('parent_link'), item.get('article_link'), item.get('crawled_time')))
            # self.c.execute('INSERT INTO NEWS_DATA(headline,contents,parent_link,article_link,crawled_time)' +
            #    'values(?,?,?,?,?);',tuple(item[k] for k in item.keys())))

            # 로그
            spider.logger.info('Item to DB inserted')
            return item
        else:
            raise DropItem('Dropped Item. Beacause This Contents is Empty')

    # 마지막 1회 실행
    def close_spider(self, spider):
        spider.logger.info('NewSpider Pipeline Stopped.')
        # pass
        # 커밋
        self.conn.commit()
        # 연결해제
        self.conn.close()
