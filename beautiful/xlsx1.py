import openpyxl

# Workbook()으로 엑셀 파일 생성
excel_file = openpyxl.Workbook()

# 엑셀 파일이 생성되면 디폴트 시트가 생성되며, 엑셀파일변수.active 로 해당 시트 선택
excel_sheet = excel_file.active
# 시트의 이름 변경
# excel_sheet.title = '리포트'

# 데이터 추가하기(행 단위로 붙음)
excel_sheet.append(['data1', 'data2', 'data3'])

# 엑셀 파일 저장
excel_file.save('c:/tmp.xlsx')

# 엑셀 파일 닫기
excel_file.close()
