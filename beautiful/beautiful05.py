# 로그인 후 데이터 수집하기

import requests as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# 로그인할 때 보내는 formData
login_info = {
    'redirectUrl': 'http://www.danawa.com/',
    'loginMemberType': 'general',
    'id': 'pjky5',
    'isSaveId': 'true',
    'password': '12341234a1'
}

# Headers 정보
headers = {
    "User-Agent": UserAgent().chrome,
    # request header에 있는 정보
    "Referer": "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F"
}

# 세션을 열어 로그인 성공 여부 확인
with req.session() as s:
    # Request(로그인 시도)
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)

    # 로그인 시도 실패 시 예외
    if res.status_code != 200:
        raise Exception("Login failed")

    # 본문 수신 데이터 확인
    # 로그인 실패시 에러메세지를 띄우고 로그인 페이지에 머무르고 있는 상태임
    print(res.content.decode('UTF-8'))

# 여기까지 작성하고 1차 확인하기
