import time
import multiprocessing


def task(lock):
    print("开始")
    with open('f1.txt', mode='r', encoding='utf-8') as f:  # 写出
        current_num = int(f.read())
    print("排队抢票")
    current_num -= 1
    with open('f1.txt', mode='w', encoding='utf-8') as f:  # 写入
        f.write(str(current_num))
    lock.release()  # 释放进程锁


if __name__ == '__main__':
    multiprocessing.set_start_method("spawn")  # 创建进程
    lock = multiprocessing.RLock()  # 进程锁
    for i in range(10):  # 创建10个子进程
        p = multiprocessing.Process(target=task, args=(lock,))
        p.start()  # 开启子进程

    time.sleep(7)  # 只有让子进程执行完了，才让它继续往下走，才不会报错
