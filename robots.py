import requests

urls = ["https://www.naver.com/", "https://www.python.org/"]

file_name = "robots.txt"

for url in urls:
    print(url+file_name)
    robots = requests.get(url+file_name)
    print(robots.text)
