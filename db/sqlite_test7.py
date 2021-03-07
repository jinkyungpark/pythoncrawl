import sqlite3
from datetime import datetime

# database 연결
conn = sqlite3.connect("./db/test.db", isolation_level=None)

# 커서 획득
cursor = conn.cursor()

# 데이터 조회
# param1 = (3,)
# cursor.execute('SELECT * FROM users WHERE id = ?', param1)
# print('param1', cursor.fetchone())
# print('param1', cursor.fetchall())

# 데이터 조회 - % 를 활용한 format 사용 가능
# param2 = 4
# cursor.execute('SELECT * FROM users WHERE id = %s' % param2)
# print('param2', cursor.fetchone())
# print('param2', cursor.fetchall())

# where절에 Dic 형태로 지정하여 가져온 경우
# cursor.execute('SELECT * FROM users WHERE id =:Id', {"Id": 5})
# print('param3', cursor.fetchone())
# print('param3', cursor.fetchall())

# where절에 두 개
# param4=(3,5)
# cursor.execute('SELECT * FROM users WHERE id IN (?,?)', param4)
# print('param4', cursor.fetchall())

# where절에 두 개
# cursor.execute('SELECT * FROM users WHERE id IN ("%d","%d")' % (3,5))
# print('param5', cursor.fetchall())


# where절에 두 개
# cursor.execute('SELECT * FROM users WHERE id=:id1 OR id=:id2',
#                {"id1": 2, "id2": 5})
# print('param6', cursor.fetchall())


# dump() 출력
with conn:
    with open('./db/dump.sql', 'w') as f:
        for line in conn.iterdump():
            f.write('%s\n' % line)
        print('Dump Print Complete ')

# f.close(), conn.close() 도 자동 호출됨 : with 를 사용했기 때문에

conn.close()
