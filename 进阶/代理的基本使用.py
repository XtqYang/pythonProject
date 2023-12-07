import urllib.request

url = 'http://www.baidu.com/s?wd=ip'
headers = {
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': 'BIDUPSID=94712B8EF162243DAF51C1FB9C9DFB91; PSTM=1666519046; BAIDUID=94712B8EF162243D06A1615F9CDBE306:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; kleck=fdf5a909ff162ece6e1931a10183f00c; BAIDUID_BFESS=94712B8EF162243D06A1615F9CDBE306:FG=1; BA_HECTOR=248ha5a1848524aha50l03ge1hm294l1a; ZFY=ryJhXRO5AXiORXxfbRdMrfIXdKlRltyhtce48pauOpQ:C; B64_BOT=1; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=36549_37686_37492_36885_37662_36786_37534_37500_37675_26350; baikeVisitId=dad9e523-144d-4f59-a5b6-f5bcf8669b98; H_PS_645EC=874eLetXVhDK%2F38%2Bd%2BBttimwSsOO5bhYKnge2pP%2FpBr8QUCQh%2FcStd1WHps',
    'Host': 'www.baidu.com',
    'Referer': 'https://www.baidu.com/s?wd=ip',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',}
# 请求对象定制
request = urllib.request.Request(url=url, headers=headers)
# 模拟浏览器访问服务器
# 深圳代理ip
proxies = {
    'http':'58.20.184.187:9091'
}
# 1.获取handler对象
handler = urllib.request.ProxyHandler(proxies=proxies)
# 2.获取opener对象
opener = urllib.request.build_opener(handler)
# 3.调用open方法
response = opener.open(request)

# 获取响应数据为字符串类型
content = response.read().decode('utf-8')
# 保存
print(content)
# with open('D:\code\pythonProject\wj\html\daili.html', 'w', encoding='utf-8') as fp:
#     fp.write(content)
