import re
import urllib.request
import urllib.parse


# 请求对象的定制
def create_request(page):
    if page == 1:
        url = 'https://sc.chinaz.com/tupian/index.html'
    else:
        url = 'https://sc.chinaz.com/tupian/index_'
        url = url + str(page) + ".html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    }
    request = urllib.request.Request(url=url, headers=headers)
    return request


# 获取响应数据
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


#         urllib.request.urlretrieve(it, 'D:\code\pythonProject\wj\jpg\lisa.jpg')
# 下载
def down_load(content):
    src_list = re.findall(r"//scpic*.chinaz.net/files/default/imgs/\d+-\d+-\d+/\w+.jpg", content)
    name_list = re.findall(r"alt=\"(?P<pattern>.*?)\"", content)

    for i in range(len(name_list)):
        name = name_list[i]
        src = src_list[i]
        src = "https:" + src
        urllib.request.urlretrieve(src, 'D:\code\pythonProject\wj\jpg\ ' + name + '.jpg')


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输结束的页码'))
    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(page)
        # 获取响应的数据
        content = get_content(request)
        # 下载
        down_load(content)
