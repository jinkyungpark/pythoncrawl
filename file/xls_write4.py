import openpyxl

# openpyxl WorkBook 객체 생성
excel_file = openpyxl.Workbook()

# 디폴트 시트 활성화하기
sheet1 = excel_file.active

# 데이터 저장하기
rows = [['name', '생년월일'], ['홍길동', '801020'],
        ['송혜교', '851115'], ['김지원', '860912'], ['남주혁', '880705']]

for row in rows:
    sheet1.append(row)


excel_file.save("./resource/test3.xlsx")
