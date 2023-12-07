from django.shortcuts import render
from appbook01.models import Books
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def user_list(request):
    """ 用户管理 """
    Books.objects.create()
    # 获取所有用户列表 [obj,obj,obj]
    # queryset = models.UserInfo.objects.all()
    return HttpResponse("成功")
