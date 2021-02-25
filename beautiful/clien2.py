import requests
from bs4 import BeautifulSoup
import xlsx_write as excel


# 클리앙 팁과강좌 1 페이지 타이틀 엑셀 저장
res = requests.get("https://www.clien.net/service/board/lecture")
soup = BeautifulSoup(res.content, "html.parser")

# 게시판 리스트 가져오기
data = soup.select("div.list_content > div.list_item.symph_row")


# 빈 리스트 생성
board_lists = list()

for item in data:
    # 타이틀 가져오기
    title = item.select_one(
        "div.list_title > a.list_subject > span.subject_fixed"
    )
    # 시간 가져오기
    time = item.select_one("div.list_time > span > span")

    print(title.get_text().strip(), time.get_text().strip()[:10])

    # 하나의 행 구성하기
    board_title = [title.get_text().strip(), time.get_text().strip()[:10]]
    # 리스트에 추가하기
    board_lists.append(board_title)

excel.write_excel_template("temp4.xlsx", "팁과강좌", board_lists)
