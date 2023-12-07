import json
import time

import redis

# 创建 Redis 连接
r = redis.StrictRedis(host='localhost', port=6379, db=9)
i = 0
start = 0
_ = 1694863160223
while (i < 3):
    i = i + 1
    start = start + 24
    _ = _ + 1
    # 创建请求数据
    request_data = {
        "url": f"https://www.duitang.com/napi/blog/list/by_search/?include_fields=like_count,sender,album,msg,reply_count,top_comments&kw=%E7%94%B7%E7%94%9F%E5%A4%B4%E5%83%8F&start={start}&_={_}",
    }
    # 将请求数据转换为 JSON 格式并推送到 Redis 列表
    r.lpush('start_urls', json.dumps(request_data))
    print(f"第{i}个已推送:" + request_data["url"])
    time.sleep(2)
