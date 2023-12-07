import time
import requests
import threading

# 创建线程锁，可以创建多个
lock_object = threading.RLock()
lock_object2 = threading.Lock()  # Lock效率高但不支持死锁，就是锁了又锁
# 自定义线程
url_list = [
    ("东北F4模仿秀.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0300f570000bvbmace0gvch7lo53oog"),
    ("卡特扣篮.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f3e0000bv52fpn5t6p007e34q1g"),
    ("罗斯mvp.mp4", "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f240000buuer5aa4tij4gv6ajqg")
]


# python的线程安全有哪些？
def task(file_name, video_url):
    lock_object.acquire()  # 加锁
    res = requests.get(video_url)
    with open(file_name, mode='wb') as f:
        f.write(res.content)
        print(time.time())
    lock_object.release()  # 释放锁


for name, url in url_list:
    # 创建线程，让每个线程都去执行task函数（参数不同）
    t = threading.Thread(target=task, args=(name, url))
    t.start()
