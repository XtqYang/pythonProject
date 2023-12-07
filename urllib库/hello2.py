import http.cookiejar
import urllib.request

# 文件地址,文件不存在cookiejar.save()会自动创建
fileName = "cookie1.txt"
# MozillaCookieJar创建cookiejar, cookiejar.save()
cookiejar = http.cookiejar.MozillaCookieJar(fileName)
# 使用HTTPCookieProcessor来创建cookie处理对象handler
handler = urllib.request.HTTPCookieProcessor(cookiejar)
# 通过build_opener构建opener
opener = urllib.request.build_opener(handler)
# 访问url，访问后会自动保存cookie到cookiejar对象中
opener.open("http://www.baidu.com")
cookie = '111'
for c in cookiejar:
    cookie = cookie + c.name + "=" + c.value + ";"
# 输出cookie信息
print(cookie[:-1])
# cookiejar.save()保存文件
cookiejar.save()
