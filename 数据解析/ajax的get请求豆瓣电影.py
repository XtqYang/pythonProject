#     POST / login.php HTTP / 2
#     Host: 9881222.xyz
#         Content - Type: application / x - www - form - urlencoded
# Content - Length: 91
#
# jumpurl = index.php & lgt = 0 & step = 2 & pwuser = cvsdvcsdvcdc + + & pwpwd = 1111111 & submit.x = 19 & submit.y = 9
import requests
import json

url = 'http://9881222.xyz'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
}
data = {
    'kw': 'love'
}
# url 请求资源路径
# params 参数
# kwargs 字典
response = requests.post(url=url, data=data, headers=headers)
response.encoding = 'utf-8'
content = response.text
# json数据解析
obj = json.loads(content)
print(obj)

# 总结
# post请求,不需要编解码
# post请求的参数是data
# 不需要请求对象的定制
