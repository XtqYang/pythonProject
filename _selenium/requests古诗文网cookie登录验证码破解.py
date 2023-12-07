import requests
from bs4 import BeautifulSoup

# 难点1 _VIEWSTATE,__VIEWSTATEGENERATOR是一个可以变化的量,解决:发现这两个变化的量在页面源码中,获取页面页面源码解析即可
# 难点2 验证码
url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
}
data = {
    'wd': 'ip'
}
response = requests.get(url=url, params=data, headers=headers)
response.encoding = 'utf-8'
content = response.text
soup = BeautifulSoup(content, 'lxml')  # 解析源码获取_VIEWSTATE,__VIEWSTATEGENERATOR
viewstate = soup.select('#__VIEWSTATE')[0].attrs.get('value')  # 获取_VIEWSTATE
viewstategenerator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
code = soup.select('#imgCode')[0].attrs.get('src')  # 获取验证码图片
code_url = "https://so.gushiwen.cn" + code
# 有坑,不是同一个请求验证码不相同,用session解决
# urllib.request.urlretrieve(url=code_url, filename='code.jpg')
# # 查看验证码图片并输入到控制台,传递给code
session = requests.session()
response_code = session.get(code_url)
# 此时注意要使用二进制数据,因为我们要使用图片下载
content_code = response_code.content
# wb的模式就是将二进制的数据写入到文件
with open('code.jpg', 'wb') as fp:
    fp.write(content_code)
code_name = input('请输入你的验证码')
# 登录
url_post = ' https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
data_post = {
    '__VIEWSTATE': 'viewstate',
    '__VIEWSTATEGENERATOR': 'viewstategenerator',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '2178124593@qq.com',
    'pwd': 'hy064872',
    'code': 'code_name',
    'denglu': '登录',
}
# 这里就不能使用requests
response_post = session.post(url=url, headers=headers, data=data_post)
content_post = response_post.text
with open('gushiwen.html', 'w', encoding='utf-8') as fp:
    fp.write(content_post)
