import sqlite3
import datetime

# database 연결
conn = sqlite3.connect("./db/test.db", isolation_level=None)

# 커서 획득
cursor = conn.cursor()
print("cursor : {}".format(type(cursor)))


# 커서를 통해 sql 실행
sql = """CREATE TABLE IF NOT EXISTS users(id integer primary key, username text, 
email text, phone text, website text, regdate text)"""
cursor.execute(sql)
conn.commit()  # create table 도 필요
conn.close()
