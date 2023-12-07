'''
适用：1080*1920
达芬奇流动：4列7行，单列上下顺序单张图片坐标
'''

# 比例:1或4
scale = 1
# 单例个数
frequency = 21
# 收尾间隔(大)
interval = 960


def d1(x):
    array1 = []
    for i in range(0, frequency):
        # 202.5为左上角ya值,67.5为左上角ya与下面一个ya的差
        ya = 202.5 - 67.5 * i
        # 480为左上角yb-ya的值
        yb = ya + interval
        s = f"({x * scale}, {ya * scale}) ({x * scale}, {yb * scale})"
        array1.append(s)
    for i in range(0, len(array1)):
        if i < 7:
            print("↑显" + str(i + 1) + "：" + array1[i])
            if i == 6:
                print()
        else:
            print("↑隐" + str(i + 1) + "：" + array1[i])


def d2(x):
    array2 = []
    for i in range(0, frequency):
        ya = -202.5 + 67.5 * i
        yb = ya - interval
        s = f"({x * scale}, {ya * scale}) ({x * scale}, {yb * scale})"
        array2.append(s)
    for j, item in reversed(list(enumerate(array2))):
        if j > 6:
            print("↓隐" + str(j + 1) + "：" + item)
            if j == 7:
                print()
        else:
            print("↓显" + str(j + 1) + "：" + item)


print("第一列向上-----------------------------------------------")
d1(x=-56)
print("第二列向下-----------------------------------------------")
d2(x=-18.625)
print("第三列向上-----------------------------------------------")
d1(x=18.625)
print("第四列向下-----------------------------------------------")
d2(x=56)
