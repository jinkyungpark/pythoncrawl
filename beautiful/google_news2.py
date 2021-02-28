# 구글 뉴스(https://news.google.com/)에서 뉴스를 검색하고
# 각 뉴스의 하이퍼링크를 수집하는 뉴스 클리핑 프로그램 작성
# %%
from bs4 import BeautifulSoup
import requests
from urllib.error import HTTPError


def main():

    try:

        keyword = input("검색어를 입력하세요 : ")

        # 요청 가져오기
        api = "https://news.google.com/search?q="+keyword+"&hl=ko&gl=KR&ceid=KR%3Ako"

        with requests.Session() as s:
            res = s.get(api)

            soup = BeautifulSoup(res.text, "html.parser")
            # 정보 추출 요청
            news_clipping = data_extract(soup)

            for news_section in news_clipping:
                for k, v in news_section.items():
                    print("{} : {}".format(k, v))
                print()
    except HTTPError as e:
        print("error", e.code)


def data_extract(soup):
    # print(soup.get_text())
    # 뉴스 섹션 영역 가져오기
    section = soup.select("div.xrnccd > article")

    # 가져온 섹션 영역에서 데이터 추출하기
    # 링크, 제목, 내용, 출처, 등록일시
    news = []
    news_item = {}
    base_url = "https://news.google.com"
    # 링크
    for item in section:
        # print("item : {}".format(item))
        # 링크와 제목을 가지고 있는 태그 지정
        link_title = item.select_one("h3 > a")
        # 링크 추출(". 이 붙어있어서")
        news_item["href"] = base_url + link_title["href"][1:]
        # 제목 추출
        news_item["title"] = link_title.get_text()
        # 내용 추출
        news_item["contents"] = item.select_one("div > span").get_text()
        # 작성일자와 시간, 작성자를 가지고 있는 태그 지정
        report_time_date_writer = item.select_one("div.QmrVtf > div.SVJrMe")
        news_item["writer"] = report_time_date_writer.select_one(
            "a").get_text()

        # time 이 없는 경우가 있음
        report_date_time = report_time_date_writer.select("time")
        # [<time class="WW6dff uQIVzc Sksgp" datetime="2020-08-26T09:38:50Z">2일 전</time>]

        if report_date_time:
            report_date_time = (report_date_time[0])["datetime"].split("T")
            news_item["report_date"] = report_date_time[0]
            news_item["report_time"] = report_date_time[1][:-1]
        else:
            news_item["report_date"] = ""
            news_item["report_time"] = ""

        # 한 섹션에 대한 정보 추가
        news.append(news_item)
        news_item = {}

    # 확인
    # print(news[:3])
    return news


if __name__ == "__main__":
    main()

# %%
