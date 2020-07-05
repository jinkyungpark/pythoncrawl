import re
import openpyxl

# 과제 (필수)
# 01_data/train.xlsx 엑셀 파일을 읽어서, 다음과 같이 이름에 들어 있는 정보를 기반으로 4개의 쉬트를 만들어 각 행의 정보를 복사하세요.
# Mr (쉬트명은 남성 : Mr.)
# Miss (쉬트명은 미혼여성 : Miss)
# Mrs (쉬트명은 기혼여성 : Mrs)
# Others (쉬트명은 기타 : 없음 )
work_book = openpyxl.load_workbook('./regex/train.xlsx')
work_sheet = work_book.active

# 파일 작성
# 4개의 시트 작성
wb = openpyxl.Workbook()
work_sheet1 = wb.active
work_sheet1.column_dimensions['A'].width = 70
work_sheet1.title = '남성'
work_sheet2 = wb.create_sheet(title='미혼여성')
work_sheet2.column_dimensions['A'].width = 70
work_sheet3 = wb.create_sheet(title='기혼여성')
work_sheet3.column_dimensions['A'].width = 70
work_sheet4 = wb.create_sheet(title='기타')
work_sheet3.column_dimensions['A'].width = 70

pattern = re.compile(r' M[ri]{1}\.{0,1}s*\.')

for each_row in work_sheet.rows:
    print(pattern.search(each_row[3].value))

    if pattern.search(each_row[3].value):    # 이 부분 반드시 필요
        if pattern.findall(each_row[3].value)[0].strip() == 'Mr.':
            work_sheet1.append([each_row[3].value])
        elif pattern.findall(each_row[3].value)[0].strip() == 'Miss.':
            work_sheet2.append([each_row[3].value])
        elif pattern.findall(each_row[3].value)[0].strip() == 'Mrs.':
            work_sheet3.append([each_row[3].value])
    else:
        work_sheet4.append([each_row[3].value])

wb.save(filename='./regex/train_gender.xlsx')


# 도전 과제 (옵션)
# 이외에 추가로 한 개 쉬트를 더 만들어서, (쉬트명은 보고서) 다음 정보를 기록하세요.
# 분류	생존자수	사망자수	생존률
# 남성	#	#	#.## %
# 미혼여성	#	#	#.## %
# 기혼여성	#	#	#.## %
# 기타	#	#	#.## %

# - 생존률은 사망자 수 / 생존자 수 + 사망자 수
# - #.## % 는 소숫점 두자리수까지 표기하라는 의미로 예를 들어 32.12 % 등
