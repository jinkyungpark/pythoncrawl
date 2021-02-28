from PIL import Image
from openpyxl import Workbook
from openpyxl.drawing.image import Image
# openpyxl WorkBook 객체 생성
excel_file = Workbook()

# 디폴트 시트 활성화하기
sheet1 = excel_file.active
sheet1.append(['name', '생년월일', '이미지'])
# 데이터 저장하기
rows = [['홍길동', '801020'],
        ['송혜교', '851115'], ['김지원', '860912'], ['남주혁', '880705']]

# with open("./resource/cat.png", "rb") as f:
#     prod_img = f.read()  # 이미지 요청 후 Byte 변환

# img.anchor(ws.cell('A1'))
# ws.add_image(img)

for idx, row in enumerate(rows, 2):
    img = Image('./resources/cat.png')
    img.width = 30
    img.height = 20
    sheet1.append(row)
    sheet1.add_image(img, 'C'+str(idx))


excel_file.save("./resources/test4.xlsx")
