from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent


# 로그인 할 때 보내는 formData
login_info = {
    "redirectUrl": "http://www.danawa.com",
    "loginMemberType": "general",
    "id": "pjky5",
    'isSaveId': 'true',
    "password": "12344321@a"
}

headers = {
    "User-Agent": UserAgent().chrome,
    "Referer": "https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F"
}


with requests.Session() as s:
    # 로그인
    res = s.post("https://auth.danawa.com/login", login_info, headers=headers)

    # 본문 수신 데이터 확인
    # 로그인 실패시 에러 메시지를 띄우고 로그인 페이지에 머무르고 있는 상태임
    # 상태코드로는 확인 불가 => 페이지가 있기 때문에 200 이 나오는 상태임
    print(res.text)

    # ------------------------------------- 1차 확인

    # 로그인 후 움직이는 과정은 링크를 통해서 움직이는 형태임
    # 로그인 성공 후 세션 정보를 가지고 페이지 이동
    res = s.get("https://buyer.danawa.com/order/Order/orderList",
                headers=headers)
    # 페이지 이동 후 수신 확인하기
    # print(res.text)

    soup = BeautifulSoup(res.text, "html.parser")

    # 로그인 성공 체크
    # 현재 다나와에서 아이디가 나오는 부분의 css 선택자
    # .user => strong
    check_id = soup.find("p", class_="user")
    print(check_id)

    if check_id is None:
        raise Exception("Login 실패, 잘못된 입력")

    # 상단 메뉴 가져오기
    info_list = soup.select("div.sub_info > ul.info_list > li")
    # print(info_list)

    # 이렇게 가져온 데이터를 파일로 저장하거나, 데이터베이스 저장, 엑셀 저장
    # 이런 일들을 할 수 있음
    print()
    print("**** My Order Info ****")
    for item in info_list:
        # 속성 메소드 확인
        # 필요한 텍스트 추출
        proc, val = item.find("span").string.strip(
        ), item.find("strong").string.strip()
        print("{} : {}".format(proc, val))
