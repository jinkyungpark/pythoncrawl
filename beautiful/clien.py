import requests
from bs4 import BeautifulSoup


for page_num in range(5):
    if page_num == 0:
        res = requests.get('https://www.clien.net/service/board/lecture')
    else:
        res = requests.get(
            'https://www.clien.net/service/board/lecture?od=T31&po='+str(page_num))

    soup = BeautifulSoup(res.content, 'html.parser')

    titles = soup.select(
        'div.list_title > a.list_subject > span.subject_fixed')
    for item in titles:
        print(item.get_text())
    print()
