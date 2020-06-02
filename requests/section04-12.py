# requests 사용 스크랩핑
# REST API : GET, POST, PUT : UPDATE, REPLACE(FETCH :UPDATE, MODIFY), DELETE
# 중요 : url 을 활용해서 자원의 상태 정보를 주고 받는 모든 것을 의미

import requests
import json

# post 방식으로 요청 / timeout 부여
with requests.Session() as s:     
    # 요청    
    r = s.delete('https://jsonplaceholder.typicode.com/posts/1')    
    
    print(r.headers)
    # 출력
    print(r.text)


    