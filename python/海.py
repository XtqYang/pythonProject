import json
import re
import base64
import requests
import urllib.parse

i = 0
while i < 10:
    url = input("输入链接")
    pid = re.findall(r'pid=(\d+)', url)[0]
    url = 'https://hjf3f3e.com/api/topic/' + pid
    proxies = {
        'http': 'http://127.0.0.1:7890',
        'https': 'http://127.0.0.1:7890'
    }
    response = requests.get(url, proxies=proxies)
    data = response.json()['data']
    # 3次base64解码和url解码
    for i in range(3):
        data = base64.b64decode(data).decode()
    data = urllib.parse.unquote(data)
    data = json.loads(data)
    DataStr = data.get('attachments')
    # 定义以m3u8结尾的url
    m3u8_url = ""
    # 遍历列表中的所有字典
    for item in DataStr:
        # 检查remoteUrl是否以m3u8结尾
        if item['remoteUrl'].endswith('m3u8'):
            # 如果以m3u8结尾，则保存remoteUrl
            m3u8_url = item['remoteUrl']
    # 请求m3u8文件并保存为字符串
    r = requests.get(m3u8_url)
    m3u8_str = r.text
    # 使用正则表达式匹配.ts文件地址
    pattern = re.compile(r'https?://.+\.ts')
    ts_url = pattern.findall(m3u8_str)[0]
    m3u8_url = "https://p.hjpfe1.com/hjstore/video/20230106/25f5b8ac94ed49f392da6ff946a7f16f/125807_i_preview.m3u8"
    ts_name = "3973563DV0AmX3W_i0.ts"

    # 去掉下划线和数字
    new_ts_name = ts_name.split("_")[0] + "_i"
    # 替换m3u8_url后面的内容
    new_url = m3u8_url[:m3u8_url.rfind('/') + 1] + new_ts_name + m3u8_url[m3u8_url.rfind('.'):]
    i += 1
    print(new_url)
