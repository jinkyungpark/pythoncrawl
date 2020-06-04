# urlopen 함수기초 사용법
# 앞에서 urlretrieve 로 했던 작업을 urlopen 으로 실행

import urllib.request as req
# 웹에서 발생할 수 있는 에러를 처리하기 위한 두 개의 객체 가져오기
from urllib.error import URLError, HTTPError

# 다운로드 경로 및 파일명
path_list = ["C:/download/dog.jpg", "c:/download/naver.html"]

# 다운로드 받을 이미지및 파일 지정
target_url = ['http://cafefiles.naver.net/20100408_237/oyehyun0123_1270726534485BsuIl_jpg/%B0%AD%BE%C6%C1%F6%A4%BE%A4%BE%A4%BE_oyehyun0123.jpg',
              'https://www.naver.com/']


#
for i, url in enumerate(target_url):
    # 예외처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)

        # 수신 내용 읽어오기
        # 이전 예제에서 읽어올 바이트수 지정했던 것과 같은 형태
        contents = response.read()

        print("-----------------------------------------------------")

        # 상태 정보 중간 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('Http status code : {}'.format(response.getcode()))
        print()
        print("-----------------------------------------------------")

        # 파일 저장 : w(write), b(byte)
        with open(path_list[i], 'wb') as c:
            c.write(contents)

    except HTTPError as e:  # 파일 다운로드 시 발생할 수 있는 에러
        print("Download Failed")
        print("HttpError code : ", e.code)
    except URLError as e:
        print("Download Failed")
        print("URL Error code : ", e.reason)
    # 성공
    else:
        print()
        print('Download Succeed')
