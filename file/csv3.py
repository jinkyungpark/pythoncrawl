# CSV : MIME - text/csv
import csv
# [예제2]
with open("./resource/sample1.csv", "r") as f:
    # 한 행을 기준으로 Dict 형태로 변환
    reader = csv.DictReader(f)
    next(reader)  # 헤더명 없애기

    for c in reader:
        print(c)
        for k, v in c.items():
            print(k, v)
        print("-----------------")
