import pymysql

# database 연결
conn = pymysql.connect(host="localhost", port=3306, user="biguser1",
                       password="12345", db="bigdata", charset="utf8")

# 커서 획득
cursor = conn.cursor()
print("cursor : {}".format(type(cursor)))


# 커서를 통해 sql 실행
sql = """
    INSERT INTO users(username,email,phone,website)
    VALUES('hong', 'hong@gmail.com', '010-1234-4321', 'hong.com')
    """
cursor.execute(sql)
conn.commit()
conn.close()
