import openpyxl

# 엑셀파일 저장하는 부분 함수 작성


def write_excel_template(filename, sheetname, listdata):

    # Workbook()으로 엑셀 파일 생성
    excel_file = openpyxl.Workbook()

    # 엑셀 파일이 생성되면 디폴트 시트가 생성되며, 엑셀파일변수.active 로 해당 시트 선택
    excel_sheet = excel_file.active
    # 엑셀 시트의 컬럼 너비 조정
    excel_sheet.column_dimensions['A'].width = 70

    # 디폴트 시트를 활성화 시켰기 때문에 Sheet 라는 이름을 가지고 있음
    if excel_sheet.title != '':
        # 시트의 이름 변경
        excel_sheet.title = sheetname

    # 데이터 추가하기(행 단위로 붙음)
    for item in listdata:
        excel_sheet.append(item)

    # 엑셀 파일 저장
    excel_file.save('c:/'+filename)

    # 엑셀 파일 닫기
    excel_file.close()
