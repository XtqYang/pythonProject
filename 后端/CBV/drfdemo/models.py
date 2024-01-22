from django.db import models


# Create your models here.

class Student(models.Model):
    """ 学生表 """
    name = models.CharField(max_length=100, verbose_name="姓名")
    sex = models.BooleanField(default=1, verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄", null=True)
    class_null = models.CharField(max_length=5, verbose_name="班级编号", null=True)
    description = models.TextField(max_length=1000, verbose_name="描述")

    class Meta:
        db_table = "tb_student"
        verbose_name = "学生"
        verbose_name_plural = verbose_name


class Publish(models.Model):
    pass
