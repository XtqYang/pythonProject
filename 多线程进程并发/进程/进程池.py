import time
from concurrent.futures import ProcessPoolExecutor
import multiprocessing


def task(num):
    print("子任务", multiprocessing.current_process().pid)
    print("执行", num)
    return num


def done(res):
    print(multiprocessing.current_process().pid)
    time.sleep(1)
    print(res.result())
    time.sleep(2)


if __name__ == '__main__':
    pool = ProcessPoolExecutor(8)  # 创建进程池，最多维护4个进程
    for i in range(10):
        fur = pool.submit(task, 2)  # 提交一个可调用对象，用给定的参数执行。
        fur.add_done_callback(done)  # 前面的进程执行完后执行

        print(multiprocessing.current_process().pid)
        pool.shutdown(True)
