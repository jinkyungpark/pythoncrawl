import sqlite3
from datetime import datetime

# database 연결
conn = sqlite3.connect("./db/test.db", isolation_level=None)

# 커서 획득
cursor = conn.cursor()

# 데이터 삭제
sql = """
    delete from users
    """
cursor.execute(sql)

# 삭제된 데이터 수 확인
print("users db deleted : ", cursor.rowcount)
conn.commit()
conn.close()
