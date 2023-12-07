import random
import time
from concurrent.futures import ThreadPoolExecutor


def task(video_url, unm):
    print("开始执行", video_url)
    time.sleep(2)
    return random.randint(0, 10)  # 产生0到10的随机数


pool = ThreadPoolExecutor(10)  # 创建线程池，最多维护10个线程
url_list = ["www.baidu.com".format(i) for i in range(30)]

for url in url_list:
    future = pool.submit(task, url, 2)  # 提交一个可调用对象，用给定的参数执行。

print("执行中。。。")
pool.shutdown(True)  # 等待线程池中的任务执行完毕后，在继续执行
print("执行完了")
