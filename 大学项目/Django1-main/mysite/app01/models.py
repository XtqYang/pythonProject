from django.db import models


# python manage.py makemigrations
# python manage.py migrate

# 对数据库操作
class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField(default=2)
    # size = models.IntegerField()
    # 在已经存在的表新增列，需要为该字段设置值:default=2，或允许为空：null=True,blank=True
    # age = models.IntegerField(default=2)


# 在内部相当于
"""
# 创建一张表,类名小写
create table app01_userinfo(
id bigint auto_increment primary key,默认会生成
name varchar(32),
password varchar(64),
age int
)
"""


class Department(models.Model):
    title = models.CharField(max_length=16)
