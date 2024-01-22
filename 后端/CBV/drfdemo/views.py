from django.shortcuts import render, HttpResponse

"""
最原始方法
"""
# Create your views here.
from rest_framework.views import APIView
from drfdemo.models import Student, Publish
# 序列化器
from rest_framework import serializers
# Response响应器,HttpResponse不是我们想要的
from rest_framework.response import Response


# 序列化器
class StudentSerializer(serializers.Serializer):
    # 你要序列化的字段
    # 更改名称：展示左边names，调用右边name
    names = serializers.CharField(source="name")
    sex = serializers.BooleanField()

    #
    # age = serializers.IntegerField()
    # class_null = serializers.CharField()

    def create(self, validated_data):
        # 插入记录
        instance = Student.objects.create(**self.validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.update(**validated_data)
        return instance


# 查看所有资源
class StudentView(APIView):
    """
    Serializer(instance=None,data=empty,**kwarg)
    用于序列化(服务器)是，将模型类对象传入instance参数
    用语反序列化(客户端)时，将要被反序列化的数据传入data参数
    还可以通过context参数添加额外数据
    """

    def get(self, request):
        print("StudentView正在get查看所有资源")
        student = Student.objects.all()
        # many=True 时传入的参数需要包含多个对象
        serializer = StudentSerializer(instance=student, many=True)
        print(serializer.data)
        return Response(serializer.data)

    # 添加
    def post(self, request):
        print("StudentView正在post添加")
        # 反序列化
        serializer = StudentSerializer(data=request.data)
        print(serializer)
        # 反序列化器校验
        if serializer.is_valid():
            # 插入数据
            stu = Student.objects.create(**serializer.validated_data)
            # 序列化
            ser = StudentSerializer(instance=stu, many=False)
            # 返回添加的数据
            return Response(ser.data)
        else:
            return Response(serializer.errors)


# 查看，序列化某条数据
class StudentDetailView(APIView):
    # 查看某条数据
    def get(self, request, id):
        print("StudentDetailView正在get查看所有资源")
        student = Student.objects.get(pk=id)
        # many=False 时传入的参数需要包含单个对象
        serializer = StudentSerializer(instance=student, many=False)
        return Response(serializer.data)

    # 删除某条数据
    def delete(self, request, id):
        print("StudentDetailView正在delete删除所有资源")
        Student.objects.get(pk=id).delete()
        return Response()

    # 更新某条数据
    def put(self, request, id):
        print("StudentDetailView正在put更新所有资源")
        # 序列化
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # 修改的个数
            n = Student.objects.filter(pk=id).update(**serializer.validated_data)
            print(n)
            stu = Student.objects.get(id=id)
            ser = StudentSerializer(instance=stu, many=False)
            return Response(ser.data)
        else:
            return Response(serializer.errors)


###############################################################
class PublishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publish

