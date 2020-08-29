# CSV : MIME - text/csv
import csv
# [예제4]
w = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]]

with open("./resource/sample5.csv", "w", newline="") as f:
    # 2차원 리스트를 csv로 작성하기
    wt = csv.writer(f)
    # 한꺼번에 데이터 쓰기
    wt.writerows(w)
