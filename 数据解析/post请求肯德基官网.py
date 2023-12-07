import urllib.parse
import urllib.request
import urllib.parse


# 响应头
def create_request(page):
    base_url = 'https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'
    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10'
    }
    # post请求的参数，必须要进行编码,且编码之后必须调用encode方法
    data = urllib.parse.urlencode(data).encode('utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    # 参数,post的请求参数是不会拼接在url后边,是需要放在请求对象定制的参数中
    request = urllib.request.Request(url=base_url, data=data, headers=headers)
    return request


# 获取响应数据
def get_content(request):
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content


# 下载
def down_load(page, content):
    # 下载数据到本地,open默认使用gbk编码，如果要保存汉字需要指定编码格式为utf-8
    # fp = open('D:\code\pythonProject\wj\json\douban.json', 'w', encoding='utf-8')
    # fp.write(content)
    # 另外一种写法
    with open('D:\code\pythonProject\wj\json\KFC_' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


if __name__ == '__main__':
    start_page = int(input('请输入起始页码'))
    end_page = int(input('请输结束的页码'))
    for page in range(start_page, end_page + 1):
        # 请求对象的定制
        request = create_request(page)
        # 获取响应的数据
        content = get_content(request)
        # 下载
        down_load(page, content)
