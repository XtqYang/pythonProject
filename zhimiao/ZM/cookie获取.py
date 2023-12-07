#!/usr/bin/python
# -*- coding: UTF-8 -*-
import requests
# 取消证书校验
import warnings

warnings.filterwarnings("ignore")
url = 'https://api.cn2030.com//sc/wx/HandlerSubscribe.ashx'
headers = {
    'Host': 'api.cn2030.com',
    'referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/97/page-frame.html',
}
cookies = {
}
payload = {
    'act': 'auth',
    'code': '063Qtc100cvMzP15b5400mM2ti3Qtc1g'
}
json = {
    "rawdata": "{\"nickName\":\"微信用户\",\"gender\":0,\"language\":\"\",\"city\":\"\",\"province\":\"\",\"country\":\"\",\"avatarUrl\":\"https://thirdwx.qlogo.cn/mmopen/vi_32/POgEwh4mIHO4nibH0KlMECNjjGxQUq24ZEaGT4poC6icRiccVGKSyXwibcPq4BWmiaIGuG1icwxaQX6grC9VemZoJ8rg/132\"}"
}

html = requests.post(url, headers=headers, params=payload, verify=False, cookies=cookies, json=json)
print(html.text)
