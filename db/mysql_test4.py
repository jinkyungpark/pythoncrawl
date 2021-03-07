import pymysql

# database 연결
conn = pymysql.connect(host="localhost", port=3306, user="biguser1",
                       password="12345", db="bigdata", charset="utf8")

# 커서 획득
cursor = conn.cursor()

# 커서를 통해 sql 실행
sql = """
    INSERT INTO users(username,email,phone,website)
    VALUES(%s, %s, %s, %s)
    """
cursor.execute(sql, ('Park', 'park@naver.com',
                     '010-4321-4321', 'park.com'))
conn.commit()
conn.close()
