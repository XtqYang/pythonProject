import os
import time
import threading
import multiprocessing


def func():
    time.sleep(1)


def task(arg):  # 子进程
    # 创建10个子线程
    for i in range(10):
        t = threading.Thread(target=func())
        t.start()


if __name__ == '__main__':  # 夫进程
    print(os.getpid())  # 获取当前进程id，
    # Linux系统fork；win:spawn ; mac支持：fork和spawn（python3.8默认设置spawn）。
    multiprocessing.set_start_method("spawn")  # 创建主进程
    p = multiprocessing.Process(target=task, args=("xxx",))  # 主进程里面的子进程
    p.name = "进程1"  # 设置进程名字
    p.daemon = True  # 设置守护进程（防止数据错乱），决定进程是否等待主进程执行完毕后才关闭
    p.start()  # 开启进程，调度的是进程里面的线程
    p.join()  # t1进程执行完毕,才继续往后走
