import sqlite3
from datetime import datetime

# database 연결
conn = sqlite3.connect("./db/test.db", isolation_level=None)

# 커서 획득
cursor = conn.cursor()


# 데이터 수정1
# param1 = ('Hong', 2)  # id가 2번인 사람의 이름을 Hong 으로 변경
# cursor.execute("update users set username = ? where id = ?", param1)


# 데이터 수정2 : dict 형태로
# cursor.execute("UPDATE users SET username =:username  WHERE id =:id",{'username':'Choi','id':5})

# 데이터 수정3 : format 형태로
cursor.execute("UPDATE users SET username = '%s'  WHERE id ='%s'" % ('Min',3))


# 중간 데이터 확인
for user in cursor.execute("select * from users").fetchall():
    print(user)

conn.commit()
conn.close()
