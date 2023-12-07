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
print(x)
# URL变量
url = "https://api.cn2030.com/"
headers = {
    'Host': 'api.cn2030.com',
    'Connection': 'keep-alive',
    'Cookie': 'ASP.NET_SessionId = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2Nzg1MjEwNjUuMTQxNzQxLCJleHAiOjE2Nzg1MjQ2NjUuMTQxNzQxLCJzdWIiOiJZTlcuVklQIiwianRpIjoiMjAyMzAzMTExNTUxMDUiLCJ2YWwiOiIvOGhSQVFJQUFBQUVibTl1WlJ4dmNYSTFielZRV25FM2VWUTFZVFYyYlZWd05tdHlNME00VUhwTkFSeHZWVEkyV0hRMVRtMUdNRzEyXHJcblNWZENkbVpEVFZwdU5FYzBaelJSRFRFeE55NHhNell1TmpRdU9USUFBQUFBQUFBQSJ9.fn3jFjV5_XYXoHkkUdrZGOz86xM2UsRqlQbEbxksx5g',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat',
    'content-type': 'application/json',
    'zftsl': getZftsl(),
    'Referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/97/page-frame.html',
    'Accept-Encoding': 'gzip, deflate, br',
}
payload = {
    'act': 'User',
}
r = x.get(url=url + '/sc/wx/HandlerSubscribe.ashx', params=payload, headers=headers, verify=False)
# 获取json数据
j = json.loads(r.text)
print(j)
