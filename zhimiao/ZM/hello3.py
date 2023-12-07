# 创建数据库连接
import time
import pymysql


def _tim4():
    t = time.time()
    # 获取毫秒时间戳
    int1 = int(round(t * 1000))
    # 转换为字符串
    int1 = str(int1)
    # 截取后4位
    int_ = int1[9:13]
    return int_


def sql_tim():
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="hy064872", db="pyth")
    # 获取一个游标对象
    cursor = conn.cursor()
    return cursor


def sql_url():
    print("连接开始=" + _tim4())
    cursor = sql_tim()
    # sql语句中，用%s做占位符，参数用一个元组
    sql = "select * from school"
    # 执行数据库插入
    cursor.execute(sql)
    # 返回一条结果行
    row = cursor.fetchone()
    # 接收全部的返回结果行.row里保存的将会是查询返回全部结果.每条结果都是一个tuple类型的数据,
    # row = cursor.fetchall()
    row = str(row)
    # 去除单引号括号逗号
    sz = row.strip("(',)")
    print(sz)
    cursor.close()
    print("连接结束=" + _tim4())


i = 0
while i < 9999:
    # 必须设置延迟
    t = 0.1
    print("延时" + str(t) + "秒")
    time.sleep(1)
    sql_url()
    i += 1
# 91f3034d3f765ce68bd3be04bd4674e2