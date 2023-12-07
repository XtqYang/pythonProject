import threading

# 创建线程锁，可以创建多把
lock_object = threading.RLock()
loop = 100
number = 0


# 函数使用线程
def _add(count):
    lock_object.acquire()  # 加锁
    global number
    for i in range(count):
        number += 1
        name = threading.current_thread().getName()  # 获取当前执行线程名称
        print(name)
    lock_object.release()  # 释放锁


# 函数需要被调用才能执行
def _sub(count):
    global number
    lock_object.acquire()  # 申请锁（等待前一把锁释放）
    for i in range(count):
        number -= 1
        name = threading.current_thread().getName()  # 获取当前执行线程名称
        print(name)


# 创建线程
t1 = threading.Thread(target=_add, args=(loop,))  # 分片执行

t2 = threading.Thread(target=_sub, args=(loop,))

t1.setName('线程1')  # 为线程设置名称

t2.setName('线程2')

t1.setDaemon(True)  # 守护线程（防止数据错乱）,决定线程是否等待主线程执行完毕才后关闭
t1.start()  #进程准备就绪，等待CPU调度
t2.start()

t1.join()  # t1线程（子线程）执行完毕,才继续往后走
t2.join()  # t2线程执行完毕,才继续往后走
print(number)
