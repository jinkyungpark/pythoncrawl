# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑

import urllib.request as req

# 파일 URL
img_url = 'http://cafefiles.naver.net/20120611_289/kkas_nknk55_1339391180925I3qnD_JPEG/%B0%ED%BE%E7%C0%CC9.jpg'
# 구글 메인 페이지 소스 다운로드 하기
html_url = 'http://google.com'

# 다운받을 경로
save_path1 = 'c:/test1.png'
save_path2 = 'c:/index.html'


# 예외 처리
# headers 값과 요청 내용 받아오기
try:
    file1, header1 = req.urlretrieve(img_url, save_path1)
    file2, header2 = req.urlretrieve(html_url, save_path2)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Headers 정보 출력
    print(header1)
    print(header2)

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))
    print('Filename2 {}'.format(file2))
    print()

    # 성공
    print('Download Succeed')

