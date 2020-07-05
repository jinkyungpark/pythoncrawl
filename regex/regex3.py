import openpyxl   # 엑셀
import re  # 정규표현식
# import os

regex = re.compile(r' Mr\.')  # 맨 앞 공백 하나 영문자는 최소 1~무한대이며 마침표
# print(os.getcwd())  D:\pythoncrawl(현재 폴더)

# 엑셀 파일 로드
work_book = openpyxl.load_workbook('./regex/train.xlsx')

# 현재 Active Sheet 얻기
work_sheet = work_book.active

# search, match
for each_row in work_sheet.rows:
    if len(regex.findall(each_row[3].value)) > 0:
        # match의 경우에는 문자열 처음부터 일치해야 하기 때문에 사용 불가
        if regex.search(each_row[3].value):
            print(each_row[3].value)

work_book.close()
