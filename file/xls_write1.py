from openpyxl import Workbook

# openpyxl WorkBook 객체 생성
excel_file = Workbook()
print(excel_file.sheetnames)  # Workbook 을 생성하면 기본 시트가 하나 작성됨


# 생성된 객체를 이용해 파일 작성
excel_file.save("./resources/test1.xlsx")
