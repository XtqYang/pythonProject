def d1():
    # 第一列
    x1 = -800
    array1 = []
    for i in range(0, 16):
        ya = -1671 + 552 * i
        yb = ya - 6768
        s = f"({x1}, {ya}) ({x1}, {yb})"
        array1.append(s)
    # 向下
    for j, item in reversed(list(enumerate(array1))):
        if j < 7:
            print("↓显" + str(j + 1) + item)
        else:
            print("↓隐" + str(j + 1) + item)


def d2():
    # 第二列
    x = -267
    array2 = []
    for i in range(0, 16):
        ya = 1641 - 552 * i
        yb = ya + 6768
        s = f"({x}, {ya}) ({x}, {yb})"
        array2.append(s)
    # 向上
    for i in range(0, len(array2)):
        if i < 7:
            print("↑显" + str(i + 1) + "个：" + array2[i])
        else:
            print("↑隐" + str(i + 1) + "个：" + array2[i])

d2()
print()
d1()
