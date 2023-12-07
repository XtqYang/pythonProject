import multiprocessing
import urllib.request
import urllib.error

# 获取ip
import requests
from lxml import etree


def _ip():
    url_ip = 'http://www.ip111.cn/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    request = urllib.request.Request(url=url_ip, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    tree = etree.HTML(content)
    return tree.xpath('normalize-space(/html/body/div[3]/div[1]/div[1]/div[2]/p[1]/text())')


proxy = {
    'http': '61.164.39.68:53281'
}


def fun1(a):
    b = a
    print("fun1开始执行")
    while a > 0:
        url = 'https://www.nsu.edu.cn/'
        requests.get(url=url, proxies=proxy)
        a -= 1
        print("fun1第%d次" % (b - a))
    print(_ip())


def fun2(a):
    b = a
    print("fun2开始执行")
    while a > 0:
        url = 'https://www.nsu.edu.cn/'
        requests.get(url=url, proxies=proxy)
        a -= 1
        print("fun2第%d次" % (b - a))
    print(_ip())


def fun3(a):
    b = a

    print("fun3开始执行")
    while a > 0:
        url = 'https://www.nsu.edu.cn/'
        requests.get(url=url, proxies=proxy)
        a -= 1
        print("fun3第%d次" % (b - a))
    print(_ip())


def fun4(a):
    b = a
    print("fun4开始执行")
    while a > 0:
        url = 'https://www.nsu.edu.cn/'
        requests.get(url=url, proxies=proxy)
        a -= 1
        print("fun4第%d次" % (b - a))
    print(_ip())


def fun5(a):
    b = a
    print("fun5开始执行")
    while a > 0:
        url = 'https://www.nsu.edu.cn/'
        requests.get(url=url, proxies=proxy)
        a -= 1
        print("fun5第%d次" % (b - a))
    print(_ip())


def fun6(a):
    b = a
    print("fun6开始执行")
    while a > 0:
        url = 'https://www.nsu.edu.cn/'
        requests.get(url=url, proxies=proxy)
        a -= 1
        print("fun6第%d次" % (b - a))
    print(_ip())


if __name__ == '__main__':
    num = 5
    p1 = multiprocessing.Process(target=fun1, args=(num,))  # 实例化进程对象
    p2 = multiprocessing.Process(target=fun2, args=(num,))
    p3 = multiprocessing.Process(target=fun3, args=(num,))
    p4 = multiprocessing.Process(target=fun4, args=(num,))
    p5 = multiprocessing.Process(target=fun5, args=(num,))
    p6 = multiprocessing.Process(target=fun6, args=(num,))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
