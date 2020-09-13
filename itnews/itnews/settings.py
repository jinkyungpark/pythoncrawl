# from fake_useragent import UserAgent

BOT_NAME = 'itnews'

SPIDER_MODULES = ['itnews.spiders']
NEWSPIDER_MODULE = 'itnews.spiders'


# USER_AGENT = UserAgent().chrome

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 다운로드 간격
DOWNLOAD_DELAY = 2

# 쿠키 사용
COOKIES_ENABLED = True


# Feferer 삽입
DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://news.daum.net'
}

# 재시도 횟수
RETRY_ENABLED = True
RETRY_TIMES = 2

# 인코딩
FEED_EXPORT_ENCODING = 'utf-8'

# 파이프라인 활성화
# 숫자가 적을 수록 우선순위 상위
ITEM_PIPELINES = {
    'itnews.pipelines.ItnewsPipeline': 300
}


# 미들웨어 설정
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}
