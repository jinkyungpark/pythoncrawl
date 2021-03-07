import pymysql

# database 연결
conn = pymysql.connect(host="localhost", port=3306, user="biguser1",
                       password="12345", db="bigdata", charset="utf8")

# 커서 획득
cursor = conn.cursor()

# 데이터 수정 : format 형태로
cursor.execute("UPDATE users SET username = %s  WHERE id = %s", ('Min', 1))


# 중간 데이터 확인
cursor.execute("select * from users")
for user in cursor.fetchall():
    print(user)

conn.commit()
conn.close()
