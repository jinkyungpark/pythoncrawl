import pymysql


class GmarketbestPipeline:
    def __init__(self):
        self.conn = pymysql.Connect(
            host="localhost", port=3306, user="root", passwd="12345", db="ecommerce", charset="utf8")
        if self.conn:
            print("Connection 성공")
        else:
            print("Connection 실패")

        self.cursor = self.conn.cursor()

    def open_spider(self, spider):
        spider.logger.info("GmarketBest Pipeline Started")

        sql = """
            CREATE TABLE IF NOT EXISTS product(
                item_code varchar(20) not null primary key,
                title varchar(200) not null,
                ori_price int not null,
                dis_price int not null,
                discount_percent int not null                 
            )
        """
        self.cursor.execute(sql)

        sql = """
            CREATE TABLE IF NOT EXISTS ranking(
                num int auto_increment not null primary key,
                main_category varchar(50) not null,
                sub_category varchar(50) not null,
                item_ranking tinyint unsigned not null,
                item_code varchar(20) not null
            )
        """
        self.cursor.execute(sql)

    # item : Item으로 작성한 것들이 하나하나 통과하게 되는 것
    def process_item(self, item, spider):

        sql = """
            insert into product(item_code,title,ori_price,dis_price,discount_percent)
            values(%s,%s,%s,%s,%s);
        """
        values = (item.get('item_code'), item.get("title"), int(item.get(
            'ori_price')), int(item.get('dis_price')), int(item.get('discount_percent')))

        self.cursor.execute(sql, values)

        sql = """
            insert into ranking(main_category, sub_category,item_ranking,item_code)
            values(%s,%s,%s,%s);
        """
        values = (item.get("main_cate_name"), item.get('sub_cate_name'),
                  int(item.get('ranking')), item.get('item_code'))

        self.cursor.execute(sql, values)

        self.conn.commit()
        return item

    def close_spider(self, spider):
        spider.logger.info("GmarketBest Pipeline Stopped")
        self.conn.close()
