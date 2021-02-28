# CSV : MIME - text/csv
import csv
# [예제2]
with open("./resources/sample2.csv", "r") as f:
    reader = csv.reader(f, delimiter="|")
    next(reader)  # 헤더명 없애기
    # 확인
    print(reader)
    print(type(reader))
    print(dir(reader))
    print()

    for c in reader:
        print(c)
