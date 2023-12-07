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


fiddler_proxies = {
    'http': 'http://127.0.0.1:8080',
    'https': 'http://127.0.0.1:8080'
}

x = requests.Session()
print(x)
# URL变量
url = "http://api.cn2030.com//sc/wx/HandlerSubscribe.ashx"

headers = {
    'Host': 'api.cn2030.com',
    'Connection': 'keep-alive',
    'Content-Length': '278',
    'referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/97/page-frame.html',
    'xweb_xhr': '1',
    'Cookie': '',
    'zftsl': getZftsl(),
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF XWEB/6500',
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh',

}
date = {
    "rawdata": "{\"nickName\":\"微信用户\",\"gender\":0,\"language\":\"\",\"city\":\"\",\"province\":\"\",\"country\":\"\",\"avatarUrl\":\"https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132\"}"
}

payload = {
    'act': 'auth',
    'code': '093Je32008fHAP1FpT000OyQo42Je32b'
}
r = x.post(url=url, params=payload, headers=headers, data=date, verify=False)
# 获取json数据
j = json.loads(r.text)
print(j)
