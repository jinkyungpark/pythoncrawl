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
    'password': '12341234a!'
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
    # print(res.content.decode('UTF-8'))

# 여기까지 작성하고 1차 확인하기

    # 로그인 후 움직이는 과정은 링크를 통해서 움직이는 형태임
    # 로그인 성공 후 세션 정보를 가지고 페이지 이동
    res = s.get(
        "https://buyer.danawa.com/order/Order/shopOrders/viewType/orderList", headers=headers)

    # 페이지 이동 후 수신데이터 확인
    # print(res.text)

# ---------------------- 2차 확인

soup = BeautifulSoup(res.text, 'html.parser')

# 로그인 성공 체크

# 현재 다나와에서 아이디가 나오는 부분의 css 선택자
# .user > strong

check_id = soup.find("p", class_='user')
# print(check_id)

if check_id is None:
    raise Exception('Login Failed. Wrong Input')


# ---------------------- 3차 확인

# 선택자 사용
# 입금 대기 /결제완료 / 배송중 이런 값들 가져오기

info_list = soup.select("div.sub_info > ul.info_list > li")
print(info_list)

# ---------------------- 4차 확인

# 여기부분에서 가져온 데이터를 파일저장, 데이터베이스 저장, 엑셀 저장
# 이런 일을 시킬 수 있음

print()
print("**** My Order Info ****")

for item in info_list:
    # 속성 메소드 확인
    # 필요한 텍스트 추출
    proc, val = item.find('span').string.strip(
    ), item.find('strong').string.strip()
    print('{} : {}'.format(proc, val))

# ---------------------- 5차 확인
