from django.conf import settings
import hashlib


def md5(data_string):
    # SECRET_KEY是Django自带的随机字符串
    obj = hashlib.md5(settings.SECRET_KEY.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    return obj.hexdigest()
# import hashlib
#
# def custom_md5(input_string):
#     # 自定义哈希逻辑，这里使用SHA-256示例
#     hasher = hashlib.sha256()
#     hasher.update(input_string.encode('utf-8'))
#     return hasher.hexdigest()
