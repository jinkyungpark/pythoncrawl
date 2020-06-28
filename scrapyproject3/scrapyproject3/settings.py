# Scrapy settings for scrapyproject1 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapyproject3'

SPIDER_MODULES = ['scrapyproject3.spiders']
NEWSPIDER_MODULE = 'scrapyproject3.spiders'


# user-agent 설정
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 다운로드 간격
DOWNLOAD_DELAY = 2

# 쿠키 사용
COOKIES_ENABLED = True


# Referer 삽입
DEFAULT_REQUEST_HEADERS = {
    'Referer': 'https://news.daum.net/'
}

# 파이프라인 활성화
# 숫자가 작을 수록 우선순위 상위
ITEM_PIPELINES = {
    'scrapyproject3.pipelines.NewsSpiderPipeline': 300
}


# user-agent Middle Wares 사용
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware': 400,
    'scrapy_fake_useragent.middleware.RetryUserAgentMiddleware': 401,
}

# 재시도 횟수
RETRY_ENABLED = True
RETRY_TIMES = 2

# 한글쓰기(출력 인코딩)
FEED_EXPORT_ENCODING = 'utf-8'
