import pymysql

# database 연결
conn = pymysql.connect(host="localhost", port=3306, user="biguser1",
                       password="12345", db="bigdata", charset="utf8")

# 커서 획득
cursor = conn.cursor()

# [실습1] 데이터 삭제
cursor.execute("DELETE FROM users WHERE id = %d" % 3)

# [실습2] 데이터  전체 삭제
# print("users db deleted : ", cursor.execute("DELETE FROM users"))

# 중간 데이터 확인
cursor.execute("select * from users")
for user in cursor.fetchall():
    print(user)

conn.commit()
conn.close()
