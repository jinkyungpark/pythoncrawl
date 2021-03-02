import sqlite3
import datetime

# sqlite 버전 확인
print("sqlite3.version : {}".format(sqlite3.version))
print("sqlite3.sqlite_version : {}".format(sqlite3.sqlite_version))

# 삽입 날짜 생성
now = datetime.datetime.now()
print("now : {}".format(now))

# 날짜를 원하는 대로
nowDateTime = now.strftime("%Y-%m-%d %H:%M:%S")
print('nowDateTime : {}'.format(nowDateTime))
