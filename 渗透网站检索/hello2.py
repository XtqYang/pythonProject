import requests

url = 'http://cn.bing.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
}
data = {
    'wd': 'cvsdvsdvds'
}
# url 请求资源路径
# params 参数
# kwargs 字典
response = requests.get(url=url, headers=headers,data=data)
response.encoding = 'utf-8'
content = response.text
print(content)

# 总结
# 参数无需使用params传递
# 参数无需urlencode编码
# 不需要请求对象定制
# 请求资源路径中的?可以加也可以不加
