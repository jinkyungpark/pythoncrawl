import requests
from bs4 import BeautifulSoup

# 페이지 요청 - 위키피디아 서울지히철 사진 저장
# 두 번째 있는 사진 저장
with requests.Session() as s:
    res = s.get(
        "https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0")

    soup = BeautifulSoup(res.text, "html.parser")

    # 사진 영역 가져오기
    target_image = soup.select_one(
        "#mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img")
    print()
    print(target_image.get('src'))
    print(target_image['src'])

    # 사진 요청하기
    download = s.get("https:"+target_image.get('src'))

    with open("d:/image/subway2.jpg", "wb") as f:
        f.write(download.content)
