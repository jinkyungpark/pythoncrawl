# 파이썬 크롤링 기초
# urllib 사용법 및 기본 스크랩핑
# urlretrieve : 파일 직접 다운로드

import urllib.request as req

# 파일 URL
img_url = 'http://blogfiles.naver.net/20100615_12/kkchblue_12765686609822pxfs_jpg/%B0%AD%BE%C6%C1%F6_kkchblue.jpg'
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
