import re
import openpyxl

# ' VS ' 로 문자열 앞뒤를 분리해보기
pattern2 = re.compile(' [A-Z]{2} ')
splited = pattern2.split('python VS java')
print(splited)

# 주민번호의 - 기호를 * 로 바꿔서 출력하기
pattern2 = re.compile('-')
subed = pattern2.sub('*', '801210-1011323')
print(subed)

# 도전 과제 : data_kr.xlsx 를 읽어서
# 주민번호 뒷자리를 * 로 바꿔서 가려보기
# re.sub('-------', '------', each_row[1].value)
excel_file = openpyxl.load_workbook('./regex/data_kr.xlsx')
# 활성시트 가져오기
work_sheet = excel_file.active

pattern = re.compile(r'[0-9]{7}')

for each_row in work_sheet.rows:
    # print(each_row[1].value)
    # print(pattern.search(each_row[1].value))
    print(re.sub(pattern, '*******', each_row[1].value))

excel_file.close()
