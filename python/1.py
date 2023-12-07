import redis
import json

try:
    r = redis.StrictRedis(host='localhost', port=6379, db=9)

    # 创建请求数据
    request_data = {
        "path": 1111111,
        "dt_url": 22222222222,
    }

    # 将请求数据转换为 JSON 格式并推送到 Redis 列表
    r.lpush('start_urls', json.dumps(request_data))
    print("数据成功推送到Redis。")
except Exception as e:
    print(f"发生错误：{str(e)}")
