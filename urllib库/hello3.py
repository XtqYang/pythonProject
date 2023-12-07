import hashlib
import time

import requests
import urllib3
from pyasn1_modules.rfc3279 import md5

md5 = hashlib.md5()
# 帮助快速禁用所有urllib3警告
urllib3.disable_warnings()
# 实例化requests.Session对象
x = requests.Session()
# URL变量
url = "https://cloud.cn2030.com"
# 设置代理
proxies = {
    'https': '127.0.0.1:8888',
    'http': '127.0.0.1:8888'
}
mxid = {}  # 需要遍历的字典 {"日期":"产品mxid"}
date_mxid = []  # 接种日期列表 ['04-17','04-18']


def getZftsl():  # 请求头获取Zftsl字段
    strtime = str(round(time.time() * 100))
    str1 = "zfsw_" + strtime
    md5.update(str1.encode("utf-8"))
    value = md5.hexdigest()
    return value


getZftsl()
