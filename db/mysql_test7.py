import pymysql

# database 연결
conn = pymysql.connect(host="localhost", port=3306, user="biguser1",
                       password="12345", db="bigdata", charset="utf8")

# 커서 획득
cursor = conn.cursor()

# 데이터 조회  - % 를 활용한 format 사용 가능
# param1 = (3,)
# cursor.execute('SELECT * FROM users WHERE id = %s' % param1)
# print('param1', cursor.fetchone())
# print('param1', cursor.fetchall())

# 데이터 조회 - % 를 활용한 format 사용 가능
# param2 = 4
# cursor.execute('SELECT * FROM users WHERE id = %s' % param2)
# print('param2', cursor.fetchone())
# print('param2', cursor.fetchall())

# where절에 두 개
cursor.execute('SELECT * FROM users WHERE id IN ("%d","%d")' % (3, 5))
print('param5', cursor.fetchall())


# 커서를 DictCursor 로 구현하면 결과는 딕셔너리 형태로 나옴
cursor1 = conn.cursor(pymysql.cursors.DictCursor)
cursor1.execute('SELECT * FROM users WHERE id IN("%d", "%d")' % (3, 5))
print('param6', cursor1.fetchall())
for row in cursor1.fetchall():
    print(row['username'])


conn.close()
