import openpyxl

# 엑셀파일에서 읽기

# 엑셀 파일 오픈
excel_file = openpyxl.load_workbook('c:/tmp2.xlsx')

# 엑셀파일 안에 있는 시트 이름 확인하기(리스트 타입으로 리턴됨)
# 시트 이름을 모르는 경우 사용
# excel_file.sheetnames

# 엑셀 파일 안에 있는 특정 시트 선택하기
# 시트 이름을 알고 있다면
excel_sheet = excel_file['기사제목']

# 시트안에 있는 데이터 읽기
for item in excel_sheet.rows:
    print(item[0].value, item[1].value)

excel_file.close()
