import pymysql

# database 연결
conn = pymysql.connect(host="localhost", port=3306, user="biguser1",
                       password="12345", db="bigdata", charset="utf8")

# 커서 획득
cursor = conn.cursor()
print("cursor : {}".format(type(cursor)))


# 커서를 통해 sql 실행
sql = """
    CREATE TABLE IF NOT EXISTS users(
        id int(11) NOT NULL AUTO_INCREMENT,
        username varchar(20),
        email varchar(100),
        phone varchar(100),
        website varchar(100),
        regdate timestamp DEFAULT CURRENT_TIMESTAMP,        
        PRIMARY KEY(id)
);
"""

cursor.execute(sql)
conn.commit()

conn.close()
