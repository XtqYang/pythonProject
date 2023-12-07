# coding=utf-8
import urllib.request
import urllib.parse
import urllib.error

# 想要爬取的地址
url = 'https://www.nsu.edu.cn'
# ua伪装
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
}
# 将周杰伦三个字变成unicode的编码格式，该方法不常用，常用urlencode
# name = urllib.parse.quote('周杰伦')
data = {
    'wd': '周杰伦',
    'sex': '男',
    'location': '中国台湾'
}

new_url = urllib.parse.urlencode(data)
url = url + new_url
# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器发起请求
response = urllib.request.urlopen(request)
# .read()一个字节一个字节的读 .decode()解码
content = response.read().decode('utf-8')
print(content)
# .readline()读取一行
content2 = response.readline().decode('utf-8')
# .readline()读取一行,直到读完
content3 = response.readlines().decode('utf-8')
# 返回url地址
geturl = response.geturl()
# 返回状态信息,以list键值对格式
getheaders = response.getheaders()
# 获取方法键值对方式
print(getheaders[1][1])
# 获取类型
type1 = type(getheaders)
