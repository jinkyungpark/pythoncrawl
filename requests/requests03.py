# requests 사용 스크랩핑
import requests

# post 방식으로 요청 / timeout 부여
with requests.Session() as s:

    # 요청
    # 데이터 보낼 때 선언한 뒤 보내기
    # payload1 = {'id': 'test777', 'pw': '1111'}  # 딕셔너리
    # r = s.post('http://httpbin.org/post', data=payload1)

    payload2 = (('id', 'test778'), ('pw', '2222'))  # 튜플(튜플로 요청시 튜플의 튜플이어야 함)
    r = s.post('http://httpbin.org/post', data=payload2)

    # 수신 상태 체크
    r.raise_for_status()  # 이 함수를 쓰면 상태 체크를 한 후 이상이 발생하면 다음 문장을 처리 안함

    # 출력
    print(r.text)

# payload2 = (('id', 'test778'), ('pw', '2222'))  # 튜플(튜플로 요청시 튜플의 튜플이어야 함)
# r = s.post('http://httpbin.org/post', data=payload2)
