from fake_useragent import UserAgent

# 객체 생성
userAgent = UserAgent()

# 브라우저 생성
print("ie", userAgent.ie)
print("msie", userAgent.msie)
print("chrome", userAgent.chrome)
print("safari", userAgent.safari)
print("opera", userAgent.opera)
print("firefox", userAgent.firefox)
print("random", userAgent.random)
