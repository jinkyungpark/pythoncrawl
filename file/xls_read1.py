# 엑셀을 처리하는 open api
# openpyxl, xlswriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(pandas 안에는 openpyxl, xlrd 가 들어있음)
# pip install xlrd
# pip install openpyxl
# pip install pandas
import openpyxl

# openpyxl을 이용해서 엑셀 파일 오픈
excel_file = openpyxl.load_workbook("./resource/sample.xlsx")
print(excel_file)
print(type(excel_file))
print(excel_file.sheetnames)

# 엑셀 파일에서 읽어올 시트 지정하기
sheet1 = excel_file['영업사원매출']
print(sheet1)

# sheet 내용 가져오기
for item in sheet1.rows:
    print(item[0].value, item[1].value,
          item[2].value, item[3].value, item[4].value, item[5].value, item[6].value)
