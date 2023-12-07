'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：579817333
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
import os, sys
import requests
import bs4
import redis

# 连接Redis
r = redis.Redis(host='127.0.0.1', password='hy064872', port=6379)

html = 'https://www.dongmanmanhua.cn/dailySchedule?weekday=MONDAY'
result = requests.get(html)
texts = result.text

data = bs4.BeautifulSoup(texts, 'html.parser')
lidata = data.select('div#dailyList ul.daily_card li')
# print(lidata)

for x in lidata:
    did = x.get('data-title-no')
    name = x.select('p.subj')
    name1 = name[0].get_text()
    url = x.a.get('href')
    story = x.a.p
    story1 = story.string
    user = x.select('p.author')
    user1 = user[0].get_text()
    like = x.select('em.grade_num')
    like1 = like[0].get_text()

    rt = {'did': did, 'name': name1, 'url': url, 'story': story1, 'user': user1, 'like': like1}

    # 写数据到Redis
    idkey = 'name' + did
    # hash表数据写入命令hmget，可以一次写入多个键值对
    r.hmget(idkey, rt)

    # 写入命令hset，一次只能写入一个键值对
    r.hset(idkey, 'did', did)
    r.hset(idkey, 'name', name1)
    r.hset(idkey, 'story', story1)
    r.hset(idkey, 'url', url)
    r.hset(idkey, 'user', user1)
    r.hset(idkey, 'like', like1)

    print('dman哈希表写入成功')
    print(r.hget(idkey, 'did'))
    print(r.hget(idkey, 'name'))
