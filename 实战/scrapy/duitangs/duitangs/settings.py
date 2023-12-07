# Scrapy settings for duitangs project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "duitangs"

SPIDER_MODULES = ["duitangs.spiders"]
NEWSPIDER_MODULE = "duitangs.spiders"

LOG_LEVEL = "WARNING"

# 配置mysql
MYSQL = {
    "host": "localhost",
    "port": 3306,
    "user": "root",
    "password": "hy064872",
    "database": "spider"
}
IMAGES_STORE = "./meinvtupian"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "duitangs.middlewares.DuitangsSpiderMiddleware": 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "duitangs.middlewares.DuitangsDownloaderMiddleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ###########################################Redis连接信息###############################
ITEM_PIPELINES = {
    # Scrapy提供了一个内置的ImagesPipeline，它包含许多用于下载、处理和存储图片的功能。
    'scrapy.pipelines.images.ImagesPipeline': 1,
    # "scrapy_redis.pipelines.RedisPipeline": 301,  # 可选
    # "duitangs.pipelines.ImgsPipeline": 300,
    "duitangs.pipelines.DuitangsPipeline": 320,
    # 'duitangs.middlewares.SeleniumMiddleware': 543,
}
# redis相关配置
REDIS_HOST = "127.0.0.1"
REDIS_PORT = 6379
REDIS_DB = 8
REDIS_PARAMS = {
    # "password", "123456"
}

# ##########################################################################################
#
#
#
# ###########################################Redis的去重和任务队列###############################
# Scrapy-redis配置信息 #固定的
# SCHEDULER = "scrapy_redis.dupefilter.RFPDupeFilter"
# SCHEDULER = "scrapy_redis.scheduler.RedisScheduler"
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"  # 去重的逻辑、要用redts的
SCHEDULER_PERSIST = True  # 如果为真。在关闭时自动保存请求信息，如果为假，则不保存请求信息

# # 布隆过滤器
# # 去重类，要使用 BLoomFilter 请替换 DUPEFILTERCLASS
DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
# # 哈希函数的个数，默认为6，可以自行修改
BLOOMFILTER_HASH_NUMBER = 6
# # B1oomFilter的 bit参数，默认30占用 128MB空间，去重量级 1 亿
BLOOMFILTER_BIT = 30
# #############################################################################################
#
#
#
# ########################################splash################################################
# 服务器地址
# SPLASH_URL = 'http://192.168.93.131:8050/'
# # 下载中间件
# DOWNLOADER_MIDDLEWARES = {
#     'scrapy_splash.SplashCookiesMiddleware': 723,
#     'scrapy_splash.SplashMiddleware': 725,
#     'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
# }
# # 去重
# SPIDER_MIDDLEWARES = {
#     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
# }
# 使用Splash的HTTP缓存
# HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
##################################################################################################
#
#
#
# ######################################Selenium#######################################################
SELENIUM_DRIVER_NAME = 'chrome'
SELENIUM_DRIVER_EXECUTABLE_PATH = 'D:/code/pythonProject/scrapy/chromedriver.exe'
# SELENIUM_DRIVER_ARGUMENTS = ['--headless']  # 如果需要无界面模式，可以添加此选项
##################################################################################################
#
#
#
##############################################延迟设置####################################################
# 将DOWNLOAD_DELAY设置为2或更高，以确保每次请求之间都有足够的延迟。
DOWNLOAD_DELAY = 0
# 将CONCURRENT_REQUESTS设置为较低的值（例如2），以同时进行的请求数量。
CONCURRENT_REQUESTS = 10
##################################################################################################
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = "httpcache"
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
