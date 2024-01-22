from rest_framework import serializers
from drfdemo.models import Student


# 创建序列化器类，会在视图中调用

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
