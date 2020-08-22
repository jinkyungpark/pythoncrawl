# requests 사용 스크랩핑
# REST API : GET, POST, PUT : UPDATE, REPLACE(FETCH :UPDATE, MODIFY), DELETE
# 중요 : url 을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미
# https://jsonplaceholder.typicode.com/ 사용

import requests

# get 방식으로 요청 / timeout 부여
with requests.Session() as s:
    r = s.get('https://api.github.com/events', timeout=0.001)
    # r = s.get('https://httpbin.org', timeout=5)

    # 수신 상태 체크
    r.raise_for_status()  # 이 함수를 쓰면 상태 체크를 한 후 이상이 발생하면 다음 문장을 처리 안함

    print(r.text)
