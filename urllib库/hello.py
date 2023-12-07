import urllib.request  # 发送请求
import urllib.parse
import ssl
import http.cookiejar  # cookie

# 添加忽略ssl证书验证
ssl._create_default_https_context = ssl._create_unverified_context
# 设置url
url = "https://www.baidu.com"
# 请求参数 data=handler
data = bytes(urllib.parse.urlencode({"data": "handler"}), "utf-8")
# 自定义头信息
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}
# 设置代理
http_proxy_handler = urllib.request.ProxyHandler({
    "http": "127.0.0.1:8080",
    'https': "http://127.0.0.1:8080"
})
# 无代理设置
# build_opener创建opener对象，传入http_proxy_handler
opener = urllib.request.build_opener(http_proxy_handler)
# 请求对象，放入请求参数，请求头等信息
request = urllib.request.Request(url, data=data, headers=headers)
# 只有opener.open()才会使用,urlopen()不会使用代理,将opener应用全局两种方式都会使用代理
response = opener.open(request)
# 得到的是httpresponse对象，read得到的是字节类型数据(只能调用一次)，需要decode()才能显示正常数据
print(response.read().decode('utf-8'))
# 获取响应头信息
print(response.getheaders())
# 返回指定响应头信息
print(response.getheader('Date'))
# 返回响应的合http状态码
print(response.getcode())
# 返回检索的URL
print(response.geturl())
# 返回网页消息头
# print(response.readinto())
# 返回文件描述信息
# print(response.fileno())
# 将opener应用全局
# urllib.request.install_opener(opener)
# response = urllib.request.urlopen(request)
# print(response.read().decode('utf-8'))
