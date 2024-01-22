"""CBV URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
# from user.views import login, LoginView
from drfdemo.views import StudentView, StudentDetailView
# from viewApp.views import AuthorView, AuthorDetailView
# from viewApp.views import PublishesView, PublishesDetailView
from viewApp.views import PublishView

urlpatterns = [
    # path("admin/", admin.site.urls),
    # path('login/', LoginView.as_view()),

    # #####################第1代Serializer#######################################
    # # 1序列化所有
    # path('student/', StudentView.as_view()),
    # # 1序列化某个
    # re_path('student3/(\d+)/', StudentDetailView.as_view()),
    #
    # # 2.序列化所有
    # path("author/", AuthorView.as_view()),
    # # 2.序列化某个
    # re_path("author/(\d+)/", AuthorDetailView.as_view()),

    # #####################第2代ModelSerializer#######################################
    # # 3.序列化所有
    # path("publishes/", PublishesView.as_view()),
    # # 3.序列化某个,?P<pk>有名参数
    # re_path("publishes/(?P<pk>\d+)", PublishesDetailView.as_view()),
    # #####################第3代视图封装viewSet#######################################
    path("publishes/", PublishView.as_view({"get": "list", "post": "create"})),
    re_path("publishes/(?P<pk>\d+)/", PublishView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

]
