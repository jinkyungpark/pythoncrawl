import sqlite3
from datetime import datetime

# database 연결
conn = sqlite3.connect("./db/test.db", isolation_level=None)

# 커서 획득
cursor = conn.cursor()

now = datetime.now()
nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

# 커서를 통해 sql 실행 1
# sql = """
#     INSERT INTO users VALUES(1, 'Kim', 'kim@naver.com', '010-1234-1234', 'kim.com',?)
#     """
# cursor.execute(sql, (nowDatetime,))  # 반드시 , 붙여야 함

# 커서를 통해 sql 실행 2
sql = """
    INSERT INTO users(username,email,phone,website,regdate)
    VALUES(?,?,?,?,?,?)
    """
cursor.execute(sql, (2, 'Park', 'park@naver.com',
                     '010-4321-4321', 'park.com', nowDatetime))
conn.commit()
conn.close()
