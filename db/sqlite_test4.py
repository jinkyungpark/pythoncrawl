import sqlite3
from datetime import datetime

# database 연결
conn = sqlite3.connect("./db/test.db", isolation_level=None)

# 커서 획득
cursor = conn.cursor()

now = datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

# 대량의 데이터 삽입 1
userList = (
    (3, 'Lee', 'lee@naver.com', '010-5321-5321', 'lee.com', nowDatetime),
    (4, 'Cho', 'cho@naver.com', '010-6321-4321', 'cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-7321-4321', 'yoo.com', nowDatetime)
)
cursor.executemany(
    "INSERT INTO users(id, username, email, phone, website, regdate) VALUES(?, ?, ?, ?, ?, ?)", userList)
conn.commit()
conn.close()
