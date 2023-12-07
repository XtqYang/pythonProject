from selenium import webdriver
from lxml import etree
import pymysql
import time

# 实例化浏览器对象
browser = webdriver.Chrome()
"""
这个文件是匹配Google Hacking搜索到的所有链接，并将其放入数据库
"""


# 对指定的url页码发起请求
def number(text, number, sleep):
    # 接收你要搜索的东西，和你要搜索这个东西多少个页面,延时
    url = 'https://www.google.com/search?q=' + text + '&ei=WartY5nJBZmSoASZiI3IBQ&start=' + str(
        number * 10 - 10) + '&sa=N&ved=2ahUKEwjZ2bfkk5n9AhUZCYgKHRlEA1kQ8tMDegQIBhAU'
    browser.get(url)
    time.sleep(sleep)
    tree = browser.page_source.encode('utf-8')
    print("正在对" + url + "发起请求")
    # 返回不规则源码
    return tree


# 存储源码
def storage(code1):
    # 接收了不规则源码
    with open('yuanma.html', 'w') as f:
        f.write(str(code1))
    # html代码书写不规范，不符合xml解析器的使用规范,使用parse方法的parser参数：
    parser = etree.HTMLParser(encoding="utf-8")
    selector = etree.parse('yuanma.html', parser=parser)
    result = etree.tostring(selector)
    result = etree.HTML(result)
    print("获取源码完成!")
    # 返回规则源码
    return result


# 获取当前页面所有网站链接
def link(code2):
    # 接收规则源码
    global li_list
    lists = []
    ints = 15
    i = 1
    print("正在正则匹配页面链接!......")
    while i < ints:
        path = '//*[@id="rso"]/div[' + str(i) + ']/div/div/div[1]/div/a/div/cite/text()'
        li_list = code2.xpath(path)
        # li_list = browser.find_element(By.XPATH, path)
        i += 1
        lists.append(li_list)
    # 返回数组
    print()
    return lists


# 去空
def emptying(lists):
    # 接收数组
    lists2 = []
    for i in lists:
        if i:
            lists2.append(i)
    # 去掉列表中的单双引号
    # 返回去空数组
    return lists2


# 判断表是否存在
def num(tab, sql_field):
    # 创建数据库连接
    mydb = pymysql.connect(host="localhost", port=3306, user="root", passwd="hy064872", db="pyth")
    # 接收你要创建的表或你要判断的表,你需要的字段
    lists = []
    mycursor = mydb.cursor()

    # 判断表是否存在
    def numb():
        mycursor.execute("SHOW TABLES")
        # 将所有表存入数据库
        for x in mycursor:
            for us in x:
                # 去除单引号括号逗号
                sz = us.strip("(',)")
                lists.append(sz)
        # 将数据库中表和你要创建的表依次进行比对
        for i in lists:
            if tab == i:
                print(tab + "表已存在!")
                # 返回是否存在标识
                return 1

    # 表不存在
    val = numb()
    if val != 1:
        print(tab + "表不存在正在创建,字段为" + sql_field)
        sql = "CREATE TABLE " + tab + " (" + sql_field + " VARCHAR(255))"
        print(sql)
        # 执行数据库插入
        mycursor.execute(sql)
        print("创建" + tab + "表成功")
    return val


# 存入数据库
def sql_url(urls, table):
    # 接收单个数据
    # 创建数据库连接
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="hy064872", db="pyth")
    # 获取一个游标对象
    cursor = conn.cursor()
    # sql语句中，用%s做占位符，参数用一个元组
    sql = "insert into " + table + " values(%s)"
    # 对应%s中的数据
    param = urls
    # 执行数据库插入
    cursor.execute(sql, param)
    # 提交
    conn.commit()
    # 关闭连接
    conn.close()
    cursor.close()


# 去重重复数据
def my_removal(sql_table, sql_field, temp):
    # 接收你要去重的表,和该表字段,和你要将去重后的数据放入哪个表
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="hy064872", db="pyth")
    # 获取一个游标对象
    cursor = conn.cursor()
    # 统计对sql_table表去重后剩余个数
    param1 = sql_table
    sql2 = "SELECT COUNT(*) AS nums FROM ((SELECT DISTINCT " + sql_field + " FROM " + sql_table + ")a);"
    cursor.execute(sql2)
    fetchall = str(cursor.fetchall())
    # 去除单引号括号逗号
    sz = fetchall.strip("(',)")
    param = int(sz)
    i = 0
    while i < param:
        # 将剩余的数据存入temp表
        sql = "INSERT INTO " + temp + " VALUES ((SELECT DISTINCT " + sql_field + " FROM " + sql_table + " limit %s,1))"
        param2 = i
        # 执行数据库插入
        cursor.execute(sql, param2)
        i += 1
    # 提交
    conn.commit()
    # 关闭连接
    conn.close()
    cursor.close()
    print("去除数据库重复数据结束")


# 删除表数据
def Delete_table_data(table_):
    print("开始删除" + table_ + "表数据")
    conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="hy064872", db="pyth")
    # 获取一个游标对象
    cursor = conn.cursor()
    sql2 = "TRUNCATE TABLE " + table_ + ""
    cursor.execute(sql2)
    conn.commit()
    conn.close()
    cursor.close()
    print("删除" + table_ + "表数据结束")


def result():
    print("开始执行")
    # 你要搜索什么
    my_index = "inurl:5433"
    # 去重后的表
    temp = "temp2"
    # 去重后的表字段
    field2 = "user"
    # 延时多少秒执行
    time_ = 4
    # 你要扫描多少个页面
    ym = 2
    # 你要创建的表，执行完后数据会删除
    table = 'test'
    # 你想要的字段
    field = "url"
    i = 0
    while i < ym:
        yuanma1 = number(text=my_index, number=i, sleep=time_)
        yuanam2 = storage(code1=yuanma1)
        shuju = link(code2=yuanam2)
        shuju2 = emptying(lists=shuju)
        # 检测表是否存在，不存在就创建
        print("正在检查存入数据表是否存在")
        num(tab=table, sql_field=field)
        print("正在检查去重后的表是否存在")
        num(tab=temp, sql_field=field2)
        print()
        print("正在将数据存入数据库中")
        for us in shuju2:
            # 去除单引号中括号
            sz = str(us)
            sz = sz.strip("[']")
            sql_url(urls=sz, table=table)
        print("第" + str(i + 1) + "页链接已存入数据库!")
        i += 1
    print()
    print("开始去除数据库重复数据")
    my_removal(sql_table=table, sql_field=field, temp=temp)
    print("执行结束已将所有数据放入" + temp + "表中")
    print()
    Delete_table_data(table_=table)


if __name__ == '__main__':
    result()
