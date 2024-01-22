from django.shortcuts import render

# Create your views here.

from rest_framework import serializers
from rest_framework.views import APIView
from viewApp.models import Author, Book, Publish
from rest_framework.response import Response


# # ################### 1.原生序列化器Serializerr######################################
# class AuthorSerializers(serializers.Serializer):
#     name = serializers.CharField(max_length=32)
#     age = serializers.IntegerField()
#
#     # 添加
#     def create(self, validated_data):
#         author_obj = Author.objects.create(validated_data)
#         return author_obj
#
#     # 更新
#     def update(self, instance, validated_data):
#         Author.objects.filter(pk=instance.pk).update(**validated_data)
#         return instance
#
#
# # 查看所有数据
# class AuthorView(APIView):
#     def get(self, request):
#         authors = Author.objects.all()
#         serializers = AuthorSerializers(instance=authors, many=True)
#         return Response(serializers.data)
#
#     def post(self, request):
#         serializers = AuthorSerializers(data=request.data)
#         # 数据校验
#         if serializers.is_valid():
#             # 向数据库Author插入数据
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)
#
#
# class AuthorDetailView(APIView):
#     def get(self, request, id):
#         author = Author.objects.get(pk=id)
#         serializers = AuthorSerializers(instance=author, many=False)
#         return Response(serializers.data)
#
#     def put(self, request, id):
#         author = Author.objects.get(pk=id)
#         serializers = AuthorSerializers(instance=author, data=request.data)
#         # 校验
#         if serializers.is_valid():
#             # 更新
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)
#
#     def delete(self, request, id):
#         Author.objects.get(pk=id).delete()
#         return Response()


# ################### 序列化器ModelSerializer######################################
# ModelSerializer帮我们重写了save
# class PublishesSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Publish
#         fields = "__all__"
#
#
# # 查看所有数据
# class PublishesView(APIView):
#     def get(self, request):
#         publish_list = Publish.objects.all()
#         serializers = PublishesSerializers(instance=publish_list, many=True)
#         return Response(serializers.data)
#
#     def post(self, request):
#         serializers = PublishesSerializers(data=request.data)
#         # 数据校验
#         if serializers.is_valid():
#             # 向数据库Author插入数据
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)
#
#
# class PublishesDetailView(APIView):
#     def get(self, request, id):
#         publishes = Publish.objects.get(pk=id)
#         serializers = PublishesSerializers(instance=publishes, many=False)
#         return Response(serializers.data)
#
#     def put(self, request, id):
#         publishes = Publish.objects.get(pk=id)
#         serializers = PublishesSerializers(instance=publishes, data=request.data)
#         # 校验
#         if serializers.is_valid():
#             # 更新
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors)
#
#     def delete(self, request, id):
#         Publish.objects.get(pk=id).delete()
#         return Response()


# # ################### 2.序列化器ModelSerializer3.升级版GenericAPIView,4.多重继承ListModelMixin######################################
# from rest_framework.generics import GenericAPIView
#
# # 多重继承ListModelMixin，封装
# """
#     CreateModelMixin创建类
#     ListModelMixin查看所有
#     RetrieveModelMixin查看单一资源
#     UpdateModelMixin更新类
#     DestroyModelMixin删除
# """
# from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
#     DestroyModelMixin
#
#
# class PublishesSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Publish
#         fields = "__all__"
#
#
# class PublishesView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     # 两个变量，变量名不能变GenericAPIView内部会使用这个变量
#     queryset = Publish.objects
#     serializer_class = PublishesSerializers
#
#     def get(self, request):
#         # serializers = self.serializer_class(instance=self.queryset, many=True)
#         # serializers = self.get_serializer_class()(instance=self.queryset, many=True)
#         # serializer = self.get_serializer(instance=self.queryset, many=True)
#         return self.list(request)
#
#     def post(self, request):
#         # serializers = self.get_serializer(data=request.data)
#         # # 数据校验
#         # if serializers.is_valid():
#         #     # 向数据库Author插入数据
#         #     serializers.save()
#         #     return Response(serializers.data)
#         # else:
#         #     return Response(serializers.errors)
#         return self.create(request)
#
#
# class PublishesDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = Publish.objects
#     serializer_class = PublishesSerializers
#
#     def get(self, request, pk):
#         # serializers = self.get_serializer(instance=self.get_object(), many=False)
#         # return Response(serializers.data)
#         return self.retrieve(request, pk)
#
#     def put(self, request, pk):
#         # serializers = self.get_serializer(instance=self.get_object(), data=request.data)
#         # # 校验
#         # if serializers.is_valid():
#         #     # 更新
#         #     serializers.save()
#         #     return Response(serializers.data)
#         # else:
#         #     return Response(serializers.errors)
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         # self.get_object().delete()
#         # return Response()
#         return self.destroy(request, pk)
#

#
# # ###################再次封装######################################
# """
#     CreateModelMixin创建类
#     ListModelMixin查看所有
#     RetrieveModelMixin查看单一资源
#     UpdateModelMixin更新类
#     DestroyModelMixin删除
# """
#
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
#
#
# class PublishesSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Publish
#         fields = "__all__"
#
#
# class PublishesView(ListCreateAPIView):
#     # 两个变量，变量名不能变GenericAPIView内部会使用这个变量
#     queryset = Publish.objects
#     serializer_class = PublishesSerializers
#
#
# class PublishesDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Publish.objects
#     serializer_class = PublishesSerializers

# # ##################视图封装ViewSetMixin(测试版)######################################
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.viewsets import ViewSetMixin
#
#
# class PublishesSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Publish
#         fields = "__all__"
#
#
# # ViewSetMixin需要放在前面
# class PublishView(ViewSetMixin, APIView):
#     def list(self, request):
#         return Response("list...")
#
#     def create(self, request):
#         return Response("create...")
#
#     def single(self, request,pk):
#         return Response("single...")
#
#     def edit(self, request,pk):
#         return Response("edit...")
# ##################视图封装ViewSetMixin最终版######################################
from rest_framework.viewsets import ModelViewSet


class PublishesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = "__all__"

    # 自定义验证规则
    def validate_name(self, value):
        if value.endswith("出版社"):
            return value
        else:
            raise serializers.ValidationError("出版社名称未以出版社结尾")


class PublishView(ModelViewSet):
    queryset = Publish.objects
    serializer_class = PublishesSerializers
