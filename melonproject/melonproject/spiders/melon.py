# -*- coding: utf-8 -*-
import scrapy


class MelonSpider(scrapy.Spider):
    name = 'melon'
    allowed_domains = ['www.melon.com/chart/index.htm']
    start_urls = ['https://www.melon.com/chart/index.htm']

    def parse(self, response):
        # print(response.text)

        songs = response.css("tbody > tr")
        idx = 1
        for song in songs:
            # print(song)
            # 노래명 //*[@id="frm"]/div/table/tbody/tr[1]/td[4]/div/div/div[1]/span/a
            title = song.css("td:nth-child(4) div.ellipsis a::text").get()

            # 가수명
            singer = song.css("td:nth-child(4) div.rank02 a::text").get()

            # 앨범명
            album = song.css("td:nth-child(5) div.rank03 a::text").get()

            # 좋아요 개수 => 동적으로 생성되서 안나옴

            print(idx, singer, title, album)
            idx += 1
            yield{
                "title": title,
                "singer": singer,
                "album": album
            }
