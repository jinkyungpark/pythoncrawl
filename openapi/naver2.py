import requests
from bs4 import BeautifulSoup
import pprint


def main():
    client_id = '6_FpNFqYVz7PeiPV7Omd'
    client_secret = 'S7f9ozjfRZ'

    naver_open_api = 'https://openapi.naver.com/v1/search/news.json'
    param = {
        'query': '코로나'
    }
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret
    }

    res = requests.get(naver_open_api, params=param, headers=headers)
    getNews(res.json())


def getNews(data):
    # pprint.pprint(data)
    for idx, item in enumerate(data['items'], 1):
        print(idx, item['link'], item['title'])


if __name__ == "__main__":
    main()
