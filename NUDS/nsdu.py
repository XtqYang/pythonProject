import re
import time
import urllib.request
import urllib.parse
import threading
from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Process
from lxml import etree


# 获取ip
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


# 发起请求,返回源码
def _request(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    return response.read().decode('utf-8')


# 正则表达式获取源码所有链接
def _screening1(test):
    file = open(test, "r", encoding='utf-8')
    data = file.read()  # read方法可以一次性 读入 并 返回文件的所有内容
    file.close()  # 关闭test.html文件
    pattern = re.compile(r'https://.*?.nsu.edu.cn')
    m = pattern.findall(data)
    return m  # 返回m链接的数组


def _screening2(test):
    file = open(test, "r", encoding='utf-8')
    data = file.read()  # read方法可以一次性 读入 并 返回文件的所有内容
    file.close()  # 关闭test.html文件
    pattern = re.compile(r'https://.*?.nsu.edu.cn')
    m = pattern.findall(data)
    return m  # 返回m链接的数组


def _screening3(test):
    file = open(test, "r", encoding='utf-8')
    data = file.read()  # read方法可以一次性 读入 并 返回文件的所有内容
    file.close()  # 关闭test.html文件
    pattern = re.compile(r'https://.*?.nsu.edu.cn')
    m = pattern.findall(data)
    return m  # 返回m链接的数组


def _screening4(test):
    file = open(test, "r", encoding='utf-8')
    data = file.read()  # read方法可以一次性 读入 并 返回文件的所有内容
    file.close()  # 关闭test.html文件
    pattern = re.compile(r'https://.*?.nsu.edu.cn')
    m = pattern.findall(data)
    return m  # 返回m链接的数组


def _screening5(test):
    file = open(test, "r", encoding='utf-8')
    data = file.read()  # read方法可以一次性 读入 并 返回文件的所有内容
    file.close()  # 关闭test.html文件
    pattern = re.compile(r'https://.*?.nsu.edu.cn')
    m = pattern.findall(data)
    return m  # 返回m链接的数组


def _screening6(test):
    file = open(test, "r", encoding='utf-8')
    data = file.read()  # read方法可以一次性 读入 并 返回文件的所有内容
    file.close()  # 关闭test.html文件
    pattern = re.compile(r'https://.*?.nsu.edu.cn')
    m = pattern.findall(data)
    return m  # 返回m链接的数组


def fun1(m1):
    T1 = time.perf_counter()
    print("fun1开始执行")
    pool = ThreadPoolExecutor(max_workers=len(m1))  # 创建线程池，最多维护m1个线程
    for url in m1:
        submit = pool.submit(func1, url)
        exception = submit.exception(2)
        if exception is None:
            print(submit, '完成')
        else:
            print(exception, "处理失败")
    T2 = time.perf_counter()
    print("fun1执行结束运行时间%.4s秒" % ((T2 - T1)))


def fun2(m2):
    T1 = time.perf_counter()
    print("fun2开始")
    pool = ThreadPoolExecutor(max_workers=len(m2))  # 创建线程池，最多维护m1个线程
    for url in m2:
        submit = pool.submit(func2, url)
        # submit.result(2)  # 如果未完成等待时间
        time.sleep(1)
        exception = submit.exception(1)
        if exception is None:
            print(submit, '完成')
        else:
            print(exception, "处理失败")
    T2 = time.perf_counter()
    print("fun2执行结束运行时间%.4s秒" % ((T2 - T1)))


def fun3(m3):
    T1 = time.perf_counter()
    print("fun3开始")
    pool = ThreadPoolExecutor(max_workers=len(m3))  # 创建线程池，最多维护m1个线程
    for url in m3:
        submit = pool.submit(func3, url)
        # submit.result(2)  # 如果未完成等待时间
        time.sleep(1)
        exception = submit.exception(1)
        if exception is None:
            print(submit, '完成')
        else:
            print(exception, "处理失败")
    T2 = time.perf_counter()
    print("fun3执行结束运行时间%.4s秒" % ((T2 - T1)))


def fun4(m4):
    T1 = time.perf_counter()
    print("fun4")
    pool = ThreadPoolExecutor(max_workers=len(m4))  # 创建线程池，最多维护m1个线程
    for url in m4:
        submit = pool.submit(func4, url)
        # submit.result(2)  # 如果未完成等待时间
        time.sleep(1)
        exception = submit.exception(1)
        if exception is None:
            print(submit, '完成')
        else:
            print(exception, "处理失败")
    T2 = time.perf_counter()
    print("fun4执行结束运行时间%.4s秒" % ((T2 - T1)))


def fun5(m5):
    T1 = time.perf_counter()
    print("fun5")
    pool = ThreadPoolExecutor(max_workers=len(m5))  # 创建线程池，最多维护m1个线程
    for url in m5:
        submit = pool.submit(func5, url)
        # submit.result(2)  # 如果未完成等待时间
        time.sleep(1)
        exception = submit.exception(1)
        if exception is None:
            print(submit, '完成')
        else:
            print(exception, "处理失败")
    T2 = time.perf_counter()
    print("fun5执行结束运行时间%.4s秒" % ((T2 - T1)))


def fun6(m6):
    T1 = time.perf_counter()
    print("fun6")
    pool = ThreadPoolExecutor(max_workers=len(m6))  # 创建线程池，最多维护m1个线程
    for url in m6:
        submit = pool.submit(func6, url)
        time.sleep(1)
        exception = submit.exception(1)
        if exception == None:
            print(submit, '完成')
        else:
            print(exception, "处理失败")
    T2 = time.perf_counter()
    print("fun6执行结束运行时间%.4s秒" % ((T2 - T1)))


def func1(url):
    print("执行func1")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    decode = response.read().decode('utf-8')
    file = open("read1.txt", "w+", encoding="utf-8")  # 源码
    file.write(decode)
    file.close()


def func2(url):
    print("执行func2")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    decode = response.read().decode('utf-8')
    file = open("read2.txt", "w+", encoding="utf-8")  # 源码
    file.write(decode)
    file.close()


def func3(url):
    print("执行func3")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    decode = response.read().decode('utf-8')
    file = open("read3.txt", "w+", encoding="utf-8")  # 源码
    file.write(decode)
    file.close()


def func4(url):
    print("执行func4")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    decode = response.read().decode('utf-8')
    file = open("read4.txt", "w+", encoding="utf-8")  # 源码
    file.write(decode)
    file.close()


def func5(url):
    print("执行func5")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    decode = response.read().decode('utf-8')
    file = open("read5.txt", "w+", encoding="utf-8")  # 源码
    file.write(decode)
    file.close()


def func6(url):
    print("执行func6")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
    }
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    decode = response.read().decode('utf-8')
    file = open("read6.txt", "w+", encoding="utf-8")  # 源码
    file.write(decode)
    file.close()


if __name__ == '__main__':
    # 主线程反源码
    url = "https://www.nsu.edu.cn/"
    request = _request(url=url)
    file = open("sound_code.txt", "w+", encoding='utf-8')
    # 写入文件
    file.write(request)
    # 读取文件
    screening1 = _screening1('sound_code.txt')  # 获取源码所有链接
    screening2 = _screening2('sound_code.txt')  # 获取源码所有链接
    screening3 = _screening3('sound_code.txt')  # 获取源码所有链接
    screening4 = _screening4('sound_code.txt')  # 获取源码所有链接
    screening5 = _screening5('sound_code.txt')  # 获取源码所有链接
    screening6 = _screening6('sound_code.txt')  # 获取源码所有链接
    print(screening1)
    print(screening2)
    print(screening3)
    print(screening4)
    print(screening5)
    print(screening6)
    p1 = Process(target=fun1, args=(screening1,))  # 实例化进程对象
    p2 = Process(target=fun2, args=(screening2,))
    p3 = Process(target=fun3, args=(screening3,))
    p4 = Process(target=fun4, args=(screening4,))
    p5 = Process(target=fun5, args=(screening5,))
    p6 = Process(target=fun6, args=(screening6,))
    p1.start()  # 进程准备就绪，等待CPU调度
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
