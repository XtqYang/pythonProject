# URL和python函数的对应关系
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    # 意思是用户访问 www.xxx.com/index/ 就会去views这个文件里面找index函数，并执行
    path("index/", views.index),
    path("index/list", views.user_list),
    path("user/add", views.user_add),
    path("user/list", views.user_list),
    path("tpl/", views.user_tpl),
    path("news/", views.news),
    # 请求和响应
    path('something/', views.something),
    # 用户登录
    path('login/', views.login),
    path('orm/', views.orm),
    # 案列
    # 显示所有用户
    path('info/list/', views.info_list),
    # 添加
    path('info/add/', views.info_add),
    # 删除
    path('info/delete/', views.info_delete)
    # 编辑
    # path('depart/list', views.depart_list),
    # path('depart/add', views.depart_add),
    # path('depart/delete', views.depart_delete),
    # path('depart/edit', views.depart_edit)
]
