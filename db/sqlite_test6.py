import sqlite3
from datetime import datetime

# database 연결
conn = sqlite3.connect("./db/test.db", isolation_level=None)

# 커서 획득
cursor = conn.cursor()

# 데이터 조회
sql = """
    select * from users
    """
cursor.execute(sql)   # 이렇게 한다고 화면에 출력되지 않음

# 조회된 데이터 출력 문구 필요
# (1, 'Kim', 'kim@naver.com', '010-1234-1234', 'kim.com', '2021-03-06 20:52:30')
print("first : ", cursor.fetchone())

print()
print("Three : ", cursor.fetchmany(size=3))  # 2,3,4번 데이터 출력

print()
# 이미 앞에서 출력을 위해 가져간 부분 제외하고 나머지
# [(5, 'Yoo', 'Yoo@naver.com', '010-7321-4321', 'yoo.com', '2021-03-06 20:52:42')]
print("All : ", cursor.fetchall())

# conn.commit()
conn.close()
