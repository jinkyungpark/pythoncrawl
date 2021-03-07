import pymysql

# database 연결
conn = pymysql.connect(host="localhost", port=3306, user="biguser1",
                       password="12345", db="bigdata", charset="utf8")

# 커서 획득
cursor = conn.cursor()

# 커서를 통해 sql 실행
userList = (
    ('Lee', 'lee@naver.com', '010-5321-5321', 'lee.com'),
    ('Cho', 'cho@naver.com', '010-6321-4321', 'cho.com'),
    ('Yoo', 'Yoo@naver.com', '010-7321-4321', 'yoo.com')
)


sql = """
    INSERT INTO users(username,email,phone,website)
    VALUES(%s,%s,%s,%s)
    """
cursor.executemany(sql, userList)
conn.commit()
conn.close()
