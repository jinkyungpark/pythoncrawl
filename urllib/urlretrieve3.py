import urllib.request as request

# 박보검
actor_url = "http://blogfiles.naver.net/MjAxOTA3MTJfMzAg/MDAxNTYyODY0MzEwMjAx.bt6BDGavCqwW0bTobR9HzZsVVuFCLRqcK59mn1i0nf0g.pDhHC9J5zHDCnOcgeKPoKqFHjajTOUVlNSz_4jS9pYkg.JPEG.juyayaya11/parkbogum-20190712-015448-001.jpg"
save_path = "c:\\actior.jpg"


# 예외 처리
# headers 값과 요청 내용 받아오기
try:
    file1, header1 = request.urlretrieve(actor_url, save_path)
except Exception as e:
    print('Download failed')
    print(e)
else:
    # Headers 정보 출력
    print(header1)

    # 다운로드 파일 정보
    print('Filename1 {}'.format(file1))

    print()

    # 성공
    print('Download Succeed')
