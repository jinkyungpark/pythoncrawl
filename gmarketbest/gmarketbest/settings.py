# Scrapy settings for gmarketbest project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'gmarketbest'

SPIDER_MODULES = ['gmarketbest.spiders']
NEWSPIDER_MODULE = 'gmarketbest.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'gmarketbest (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# 한글처리
FEED_EXPORT_ENCODING = "utf-8"

# 로그 저장
#LOG_FILE = "log.txt"

# 'dont_filter = True'와 같은 역할
# DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

# items에 저장될때 필드 순서를 지키고 싶다면?
FEED_EXPORT_FIELDS = ['main_cate_name', 'sub_cate_name',
                      'ranking', 'title', 'ori_price', 'dis_price', 'discount_percent']


# 스크래피가 동시에 크롤링 하는 갯수를 줄이면 순서대로 저장도 가능
# CONCURRENT_REQUESTS = 1
