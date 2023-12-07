# 可以用来读取配置文件
import configparser
# 获取当前时间
import datetime
# 是一种轻量级的数据交换格式
import json
# 代表了程序所在的操作系统，主要用于获取程序运行所在操作系统的相关信息。
import os
# 提供了一些接口，用于访问 Python 解释器自身使用和维护的变量
import sys
# 正则表达式
import re
# 哈希加密
import hashlib

import pymysql
# urllib3模块是一个第三方的网络请求模块。
import urllib3
# 该模块主要用来发 送 HTTP 请求
import requests.utils
import requests.cookies
import time
# 加解密
import base64
from Crypto.Cipher import AES
from Crypto.SelfTest.st_common import a2b_hex, b2a_hex
from Crypto.Util.Padding import unpad, pad
from requests.sessions import RequestsCookieJar
# 创建数据库连接
import time
import pymysql

# 获取一个md5加密算法对象
md5 = hashlib.md5()
# 帮助快速禁用所有urllib3警告
urllib3.disable_warnings()
# 实例化requests.Session对象
x = requests.Session()
print(x)
# URL变量
url = "https://api.cn2030.com"
# 设置代理
proxies = {
    'https': '127.0.0.1:8888',
    'http': '127.0.0.1:8888'
}
# 需要遍历的字典 {"日期":"产品mxid"}
mxid = {}
# 接种日期列表 ['04-17','04-18']
date_mxid = []
# 接收单个数据
# 创建数据库连接
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="hy064872", db="pyth")
# 获取一个游标对象
cursor = conn.cursor()


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


# 获取数据库内容
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
    # print(sz)
    cursor.close()
    print("连接结束=" + _tim4())
    return sz


# zftsl: 143ddf5bef3fafb3b274cc896f65b920
# 以时间戳为种子的MD5字符串，那这个字段的目的应该是为了方式抓包软件重复发送相同数据包。
# 请求头获取Zftsl字段
def getZftsl():
    # strtime = str(round(time.time() * 100))
    # str1 = "zfsw_" + strtime
    # # 制定需要加密的字符串
    # md5.update(str1.encode("utf-8"))
    # # 获取加密后的16进制字符串
    # value = md5.hexdigest()
    value = sql_url()
    return value


# Body解密，CBC模式，pkcs7填充，数据块128，偏移1234567890000000
def getDecrypt(k, value, iv=b'1234567890000000'):
    try:
        cryptor = AES.new(k.encode('utf-8'), AES.MODE_CBC, iv)
        value_hex = a2b_hex(value)
        unpadtext = unpad(cryptor.decrypt(value_hex), 16, 'pkcs7')
        j = json.loads(unpadtext)
        return j
    except Exception as e:
        print("解密错误：", e)
        return False


# Body加密，CBC模式，pkcs7填充，数据块128，偏移1234567890000000
def getEncrypt(k, value, iv=b'1234567890000000'):
    try:
        value = value.encode('UTF-8')
        cryptor = AES.new(k.encode('utf-8'), AES.MODE_CBC, iv)
        text = pad(value, 16, 'pkcs7')
        ciphertext_hex = b2a_hex(cryptor.encrypt(text))  # 字符串转十六进制数据
        ciphertext_hex_de = ciphertext_hex.decode()
        ciphertext_hex_de = ciphertext_hex.decode().strip()
        return ciphertext_hex_de
    except Exception as e:
        print("加密错误", e)
        return None


def getSign(cookie):  # 获取用户签名（用于解密）
    global Sign
    try:
        data = cookie.split('.')[1]
        missing_padding = 4 - len(data) % 4
        if missing_padding:
            data += '=' * missing_padding
        b = base64.b64decode(data.encode("utf-8")).decode("utf-8")
        b = json.loads(b)
        b = b['val'].replace(' ', '').replace('\r\n', '')
        b = base64.b64decode(b)
        b = str(b)
        j = re.findall(r'(?<=\\x00\\x00\\x10).{16}', b)[0]
        Sign = j
        return True
    except Exception as e:
        print("获取签名错误：", e)
        return False


def getHeaders():  # 返回请求头
    # 'Cookie': 'ASP.NET_SessionId=' + cookie,
    headers = {
        'Set - Cookie': 'ASP.NET_SessionId = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2Nzc2NDcxNTYuNDI2MDY0NywiZXhwIjoxNjc3NjUwNzU2LjQyNjA2NDcsInN1YiI6IllOVy5WSVAiLCJqdGkiOiIyMDIzMDMwMTEzMDU1NiIsInZhbCI6ImoxbXlBUUlBQUFBRWJtOXVaUnh2Y1hJMWJ6VkZZVEZpUzBSMVgwZGtPRWhZYWxKdU5IaExWWEIzQVJ4dlZUSTJXSFEwZFdOSGMyMTNcclxuZHpseGRsRTFVRUpOVEZnelVteGpEVEV4Tnk0eE16WXVOalF1T1RRQUFBQUFBQUFBIn0.W - a54PbyoZfKOjJs0ZvAbuR2Z62r8AL7qOza3Q92ux8',
        'Host': 'cloud.cn2030.com',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.20(0x18001433) NetType/WIFI Language/zh_CN',
        'content-type': 'application/json',
        'zftsl': getZftsl(),
        'Referer': 'https://servicewechat.com/wx2c7f0f3c30d99445/92/page-frame.html',
        'Accept-Encoding': 'gzip,deflate, br',
        # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    }
    return headers


# 返回Payload
def getPayload(p_id, id, scdate):
    payload = {
        'act': 'GetCustSubscribeDateDetail',
        'pid': p_id,
        'id': id,
        'scdate': scdate
    }
    return payload


# 获取scdate日期当天的产品列表
def getMxid(scdate):
    try:
        list1 = []
        r = x.get(url=url + '/sc/wx/HandlerSubscribe.ashx', headers=getHeaders(), params=getPayload(p_id, id, scdate),
                  timeout=1, verify=False)
        j = getDecrypt(Sign, r.text)
        if j["status"] == 200:
            if 'mxid' in str(j):
                for i in j["list"]:
                    if i['qty'] > 0:
                        list1.insert(0, i['mxid'])
                mxid[scdate] = list1
                return True
            else:
                print("GetMxid没有mxid:", j)
                return False
        else:
            print("GetMxid状态码不为200:", j)
            return False
    except Exception as e:
        print("GetMxid:", e)
        return False


# 获取疫苗可预约时间
def getDate():
    current_date = datetime.datetime.now().strftime('%Y%m')
    payload = {
        'act': 'GetCustSubscribeDateAll',
        'pid': p_id,
        'id': id,
        'month': current_date
    }
    try:
        r = x.get(url=url + '/sc/wx/HandlerSubscribe.ashx', params=payload, headers=getHeaders(), timeout=1,
                  verify=False)
        j = json.loads(r.text)
        if (j["status"] == 200):
            if ('enable' in str(j)):
                for date in j["list"]:
                    if (date["enable"] == True):
                        date_mxid.insert(0, date["date"])
                return True
            else:
                return False
    except Exception as e:
        print("获取日期失败：", e)


# 设置cookie
def set_Cookie(r):
    global cookie
    try:
        del x.cookies['ASP.NET_SessionId']
        cookies = r.cookies
        x.cookies.update(cookies)
        cookie_dict = requests.utils.dict_from_cookiejar(r.cookies)
        new_cookie = cookie_dict['ASP.NET_SessionId']
        update_config(cookie, new_cookie)
        cookie = new_cookie
        return True
    except Exception as e:
        print("cookie出错：", e)
        return False


# 请求查询是否获取验证码
def yanZheng_code(mxid):
    global r_cookie
    payload = {
        'act': 'GetCaptcha',
        'mxid': mxid
    }
    try:
        r = x.get(url=url + '/sc/wx/HandlerSubscribe.ashx', headers=getHeaders(), params=payload, verify=False,
                  timeout=1)
        j = json.loads(r.text)
        r_cookie = r
        set_Cookie(r)
        if (j['status'] == 200):
            return True
        else:
            print('状态: 有验证码：', r.text)
            return False
    except Exception as e:
        print('验证码出错：', e)
        return False


# 提交订单信息
def OrderPost(mxid, scdate):
    try:
        postContext = '{"birthday":"%s","tel":"%s","sex":%s,"cname":"%s","doctype":1,"idcard":"%s","mxid":"%s","date":"%s","pid":"%s","Ftime":1,"guid":""}' % (
        birthday, tel, sex, cname, idcard, mxid, scdate, p_id)
        postContext = getEncrypt(Sign, postContext)
        r = x.post(url=url + '/sc/api/User/OrderPost', data=postContext, timeout=1, headers=getHeaders(), verify=False)
        if ("eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9" not in r.headers.get('set-cookie')):
            set_Cookie(r_cookie)
        if (r.status_code == 200):
            j = json.loads(r.text)
            if (j['status'] == 200):
                print("状态: " + j["msg"], end='')
                return True
            else:
                print("状态: " + j["msg"], end='')
                return False
        else:
            return False
    except Exception as e:
        print("OrderPost：", e)


# 获取订单信息状态
def GetOrderStatus():
    try:
        payload = {
            'act': 'GetOrderStatus'
        }
        r = x.get(url=url + '/sc/wx/HandlerSubscribe.ashx', params=payload, headers=getHeaders(), verify=False,
                  timeout=1)
        j = json.loads(r.text)
        if (j['status'] == 200):
            print("\t结果: " + j["msg"])
            input('抢购成功！退出程序。')
            sys.exit(0)
        else:
            print("\t结果: " + j["msg"])
            return False
    except Exception as e:
        print("GetOrderStatus：", e)


# 获取用户基本信息
def getUserInfo():
    global birthday, tel, cname, sex, idcard
    payload = {
        'act': 'User'
    }
    try:
        r = x.get(url=url + '/sc/wx/HandlerSubscribe.ashx', params=payload, headers=getHeaders(), verify=False)
        # 获取json数据
        j = json.loads(r.text)
        if (j['status'] == 200):
            # 日期
            birthday = j['user']['birthday']
            # 手机号
            tel = j['user']['tel']
            # 性别
            sex = j['user']['sex']
            # 姓名
            cname = j['user']['cname']
            # 身份证号
            idcard = j['user']['idcard']
            print("登录成功，用户：", cname, end='')
            return True
        else:
            print('Cookie出错：%s' % r.text)
            input('退出程序')
            sys.exit(0)
    except Exception as e:
        print("无法正常运行", e)
        input('退出程序')
        sys.exit(0)


# 初始化配置文件
def file_config():
    global cookie  # cook,
    global wait_speed  # 等待开始刷新时间，单位毫秒
    global buy_speed  # buy_speed 抢购间隔，单位毫秒
    global p_id  # 疫苗产品id（1是九价）
    global id  # 门诊医院id
    cf = configparser.RawConfigParser()
    if (os.path.exists('jiujia.ini')):
        try:
            cf.read("jiujia.ini", encoding='utf-8')
            cookie = cf.get("jiujia", "cookie")
            wait_speed = cf.get("jiujia", "wait_speed")
            buy_speed = cf.get("jiujia", "buy_speed")
            p_id = cf.get("jiujia", "p_id")
            id = cf.get("jiujia", "id")
            c = requests.cookies.RequestsCookieJar()  # 4.设置Cookie
            c.set('ASP.NET_SessionId', cookie)
            x.cookies.update(c)
        except Exception as e:
            print("配置文件错误", e)
            input('')
            sys.exit(0)
    else:
        print("jiujia.ini配置文件不存在当前文件夹下。")
        input('')
        sys.exit(0)


# 更新配置文件中的Cookie
def update_config(old_cookie, new_cookie):
    file_data = ""
    with open('jiujia.ini', "r", encoding="UTF-8") as f:
        for line in f:
            if old_cookie in line:
                line = line.replace(old_cookie, new_cookie)
            file_data += line
    with open("jiujia.ini", "w", encoding="UTF-8") as f:
        f.write(file_data)


# 主体程序
def main():
    # 循环日期列表获取接种列表
    for i in date_mxid:
        max_retry = 0
        while max_retry < 3:
            try:
                cishu = 1
                if (getMxid(i)):
                    print("抢苗接种时间：", i)
                    for mxid_now in mxid[i]:
                        print('开始第%s次抢购 (%s) ' % (cishu, mxid_now), end='')
                        if (yanZheng_code(mxid_now)):
                            time.sleep(int(buy_speed) / 1000)
                            if (OrderPost(mxid_now, i)):
                                time.sleep(int(buy_speed) / 1000)
                                GetOrderStatus()
                                time.sleep(int(buy_speed) / 1000)
                        cishu += 1
                    break
                else:
                    time.sleep(1)
            except Exception as e:
                print(e)
                time.sleep(1)
            max_retry += 1


cookie = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NzcyNTM2ODIuMjg5MjQxNiwiZXhwIjoxNjc3MjU3MjgyLjI4OTI0MTYsInN1YiI6IllOVy5WSVAiLCJqdGkiOiIyMDIzMDIyNDIzNDgwMiIsInZhbCI6ImoxbXlBUUlBQUFBRWFHRm9ZUnh2Y1hJMWJ6VkZZVEZpUzBSMVgwZGtPRWhZYWxKdU5IaExWWEIzQUJ4dlZUSTJXSFEwZFdOSGMyMTNcclxuZHpseGRsRTFVRUpOVEZnelVteGpEakUzTVM0eU1UY3VOemd1TVRNekFBQUFBQUFBQUE9PSJ9.AYS-rdz_dP-09UDsENjjvY9Uri44hzNRuO5dR1KkIHk'
wait_speed = '1000'  # wait_speed 等待开始刷新时间，单位毫秒
buy_speed = '1000'  # buy_speed 抢购间隔，单位毫秒
p_id = '3'  # p_id 疫苗产品id（1是九价）
id = '6717'  # id 门诊医院id

if __name__ == '__main__':
    # cookie = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDk5NTY1MDIuNzk0MTMyMiwiZXhwIjoxNjQ5OTYwMTAyLjc5NDEzMjIsInN1YiI6IllOVy5WSVAiLCJqdGkiOiIyMDIyMDQxNTAxMTUwMiIsInZhbCI6IkwydlFBQUlBQUFBUVlUTTBZMlV3TUdOak5HTmtOVGN4TWh4dmNYSTFielZNY0VsRWRFMXFZMnR6UzA1ckxXTkdNelpOTldKekFCeHZcclxuVlRJMldIUTJVRlZNTVU5TlNFMTVlV1JOVDFOcGRtSnNTalJSRHpFeU5DNHlNall1TWpVeExqSXpNQUFBQUFBQUFBQT0ifQ.3-Uu3qizNJvgQDm7sTPCAEkU-Hp2lxmYwfeqIOPbaGY'

    # x.cookies['ASP.NET_SessionId'] = cookie # 1.设置Cookie

    # x.cookies.set('ASP.NET_SessionId', cookie, path='/') #2. 设置Cookie
    # x.cookies.set('path','/')

    # cookie_2 = {
    #     'ASP.NET_SessionId':cookie
    # }
    # requests.utils.add_dict_to_cookiejar(x.cookies, cookie_2) #3.设置Cookie
    print("开始初始化用户信息")
    file_config()
    print("开始获取用户信息")
    getUserInfo()
    print("开始生成解密秘钥")
    getSign(cookie)
    print('\t2022-04-17版本')

    for i in range(100):
        # 清空需要遍历的字典 {"日期":"产品mxid"}
        mxid = {}
        # 清空接种日期列表 ['04-17','04-18']
        date_mxid = []
        while not (getDate()):
            try:
                print('列表刷新：', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))
                time.sleep(int(wait_speed) / 1000)
            except Exception as e:
                print('ERROR:', e)
        print(date_mxid)
        print("开始抢苗")
        # 程序运行窗口
        main()
        print("继续努力中...")
# 关闭数据库连接
conn.close()
cursor.close()
