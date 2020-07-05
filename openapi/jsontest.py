import json

data = """
    {
        "id":"01",
        "language":"Java", 
        "edition":"third", 
        "author":"Heart Schildt",
        "history":
        [
            {
                "date":"2020-06-30",
                "item":"iPhone"
            },
            {
                "date":"2020-07-30",
                "item":"android"
            }
        ]        
    }
"""

# json 형식의 데이터를 파이썬 객체로 역직렬화
# 딕셔너리 형태로 만들어 주는 것
json_data = json.loads(data)

# 전체 데이터 출력하기
print(json_data)
# id 키 값의 value 가져오기
print(json_data['id'])

print(json_data['history'])
print(json_data['history'][0])
print(json_data['history'][0]['date'])


