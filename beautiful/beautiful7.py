# BeautifulSoup 사용 스크랩핑 - 이미지 다운로드

import os
import urllib.parse as rep
import urllib.request as req
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

# Header 정보 초기화
opener = req.build_opener()
# User-Agent 정보
opener.addheaders = [('User-Agent', UserAgent().ie)]
# Header 정보 삽입
req.install_opener(opener)

# 네이버 이미지 기본 URL(크롬 개발자)
base = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
# 검색어
quote = rep.quote_plus('호랑이')
# URL 완성
url = base + quote

# 요청 URL 확인
print('Request URL : {}'.format(url))

# Request
res = req.urlopen(url)

# 이미지 저장 경로
savePath = "c:\\imagedown\\"

# 폴더 생성 예외 처리(문제 발생 시 )
try:    
    # 기본 폴더가 있는지 체크
    if not (os.path.isdir(savePath)):
        #없으면 폴더 생성
        os.makedirs(os.path.join(savePath))
except OSError as e:
    # 에러 내용
    print('folder creation failed')
    print('folder name : {}'.format(e.filename))

    # 런타임 에러
    raise RuntimeError("System Exit")
else:
    # 폴더 생성이 되었거나, 존재할 경우
    print("folder is created!")



# bs4 초기화
soup = BeautifulSoup(res,"html.parser")

# print(soup.prettify())    # 확인용임


#  a.thumb._thumb > img
img_list = soup.select('div.img_area > a.thumb._thumb > img')
print(img_list)


# 반복문을 사용하여 이미지 경로 가져오기
for i, img in enumerate(img_list, 1):
    # 속성확인
    print()
    print()
    print(img['data-source'], i)
    # 저장 파일명 및 경로
    fullfileName = os.path.join(savePath, savePath+str(i)+'.png')
    # 파일명 확인
    # print(fullfileName)


    # 다운로드 요청(url, 다운로드 경로)
    req.urlretrieve(img['data-source'],fullfileName)

