# 클리앙 제목과 날짜 추출 후 엑셀 저장하기
from bs4 import BeautifulSoup
import requests
import xlsx_write as excel

# 빈 리스트 선언하기
board_lists = list()

# 팁과 강좌 2page
for no in range(5):
    if no == 0:
        url = 'https://www.clien.net/service/board/lecture'
    else:
        url = 'https://www.clien.net/service/board/lecture?&od=T31&po=' + \
            str(no+1)

    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')

    # 하나의 행 가져오기
    data = soup.select('div.list_content > div.list_item.symph_row')


    for item in data:
        # 가져온 하나의 행에서 타이틀과 시간 가져오기
        title = item.select_one(
            'div.list_title > a.list_subject > span.subject_fixed')
        time = item.select_one('div.list_time > span')

        # print(title.get_text())
        # print(time.get_text().strip()[:5])  # 날짜에 숨겨진 시분초까지 나와서

        # 한 행 구성하기
        board_content = [title.get_text().strip(), time.get_text().strip()[:5]]
        # 각각의 행을 붙여 시트에 붙일 상태로 만들기
        board_lists.append(board_content)

excel.write_excel_template('tmp3.xlsx', '기사제목', board_lists)
