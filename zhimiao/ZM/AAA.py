# 实例化requests.Session对象
import json
import requests
# 自定义的模块
from Mo_Kuai import sftsl
# 取消证书校验
import warnings
warnings.filterwarnings("ignore")


def getZftsl():
    return sftsl.sql_url()


x = requests.Session()
# URL变量
headers = {
    'Cookie': 'ASP.NET_SessionId=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2Nzg1MTY3MDAuODkzNjk0NCwiZXhwIjoxNjc4NTIwMzAwLjg5MzY5NDQsInN1YiI6IllOVy5WSVAiLCJqdGkiOiIyMDIzMDMxMTE0MzgwNyIsInZhbCI6Ii84aFJBUUlBQUFBRWJtOXVaUnh2Y1hJMWJ6VlFXbkUzZVZRMVlUVjJiVlZ3Tm10eU0wTTRVSHBOQUJ4dlZUSTJXSFExVG0xR01HMTJcclxuU1ZkQ2RtWkRUVnB1TkVjMFp6UlJEVEV4Tnk0eE16WXVOalF1T1RJQUVGODRhRkpCVWw4M1FVRkRObk5FVVVJQkFBQUFBQT09In0.La3z06qFJ2jKdxGVXAk7skDgn7yKjtvOhpgc1jcGb08; path=/',
    'Content-Length': '418',
    'Referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/97/page-frame.html',
    'Xweb_xhr': '1',
    'Zftsl': getZftsl(),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6500',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh',
    'Connection': 'close'
}
date = {
    "cdscdscdscsdcv"
}

r = x.post(url="http://api.cn2030.com//sc/api/User/OrderPost", headers=headers, data=str(date), verify=False)
# 获取json数据
j = json.loads(r.text)
print(j)
