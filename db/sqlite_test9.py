import sqlite3
from datetime import datetime

# database 연결
conn = sqlite3.connect("./db/test.db", isolation_level=None)

# 커서 획득
cursor = conn.cursor()

# [실습1] 데이터 삭제
cursor.execute("DELETE FROM users WHERE id = ?", (2,))

# [실습2] 데이터 삭제
cursor.execute("DELETE FROM users WHERE id = :id", {'id': 5})

# [실습3] 데이터 삭제
cursor.execute("DELETE FROM users WHERE id = %d" % 3)

print()
# 중간 데이터 확인 2
for user in cursor.execute("select * from users").fetchall():
    print(user)

# [실습4] 데이터  전체 삭제
print("users db deleted : ", cursor.execute("DELETE FROM users").rowcount)


# 중간 데이터 확인
for user in cursor.execute("select * from users").fetchall():
    print(user)

conn.commit()
conn.close()
