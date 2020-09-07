# 잘못된 데이터 제거, DB 저장, SMS 전송, 메일 전송, SNS 전송
from scrapy.exceptions import DropItem
import csv
import openpyxl


class Scrapyproject5Pipeline:

    # 초기화 메소드
    def __init__(self):
        # 엑셀 처리 선언
        self.workbook = openpyxl.Workbook()
        self.worksheet = self.workbook.active
        self.worksheet.column_dimensions['A'].width = 10
        self.worksheet.column_dimensions['B'].width = 15
        self.worksheet.column_dimensions['C'].width = 15
        self.worksheet.column_dimensions['D'].width = 20
        self.worksheet.column_dimensions['E'].width = 10
        self.worksheet.append(
            ['rank_num', 'site_name', 'daily_time', 'daily_page_view', 'is_pass'])
        # csv 처리 선언
        self.file_opener = open("./result.csv", "w", newline="")
        self.csv_writer = csv.DictWriter(self.file_opener, fieldnames=[
                                         'rank_num', 'site_name', 'daily_time_site', 'daily_page_view', 'is_pass'])
        self.csv_writer.writeheader()

    # 최초 한 번만 실행
    def open_spider(self, spider):
        spider.logger.info('Scrapyproject5Pipeline Started.')

    # item : Item으로 작성한 것들이 하나하나 통과하게 되는 것
    def process_item(self, item, spider):
        if int(item.get('rank_num')) < 41:
            # if int(item.get('rank_num')) < 11:
            item['is_pass'] = True

            # 엑셀 저장
            rank_num = item.get('rank_num')
            site_name = item.get('site_name')
            daily_time = item.get('daily_time_site')
            daily_page_view = item.get('daily_page_view')
            is_pass = item.get('is_pass')
            # print('excel', rank_num, site_name,
            #       daily_time, daily_page_view, is_pass)
            self.worksheet.append([rank_num, site_name, daily_time,
                                   daily_page_view, is_pass])

            # csv 저장
            self.csv_writer.writerow(item)
            return item
        else:
            raise DropItem(
                f'Dropped Item. Because This Site Rank is {item.get("rank_num")}')

    # 마지막 1회 실행

    def close_spider(self, spider):
        self.workbook.save("./result.xlsx")
        # 엑셀 파일 닫기
        self.workbook.close()
        # csv 닫기
        self.file_opener.close()
        spider.logger.info('Scrapyproject5Pipeline Closed.')
