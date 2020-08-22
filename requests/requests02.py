import requests

# 세션 활성화
s = requests.Session()

# 세션을 이용해 요청
data = {
    "name": "hong"
}

r = s.put("https://httpbin.org/put", data=data)

print(r.text)

# 세션 닫기
s.close()


# get 방식
# r = s.get("https://httpbin.org/get")
# print(r.text)


# post 방식
# data = {
#     "name": "hong"
# }

# r = s.post("https://httpbin.org/post", data=data)


# delete 방식
# r = s.delete("https://httpbin.org/delete")
