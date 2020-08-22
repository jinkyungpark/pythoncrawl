# requests 사용 스크랩핑
import requests

# 세션 활성화
# 여러번의 requests 요청시 같은 host 를 유지할 수 있고
# 같은 TCP connection 이용
s = requests.Session()

# 세션을 이용해 요청
# get 방식
r = s.get('https://www.naver.com')

# 수신 데이터
# print(r.text)  # r 출력시 코드만 나옴

# 수신 상태
# print('status code : {}'.format(r.status_code))

# 확인 (간단해서 자주 사용함)
print('OK ? : {}'.format(r.ok))


# 세션 종료 - 세션 비 활성화
s.close()
