from django.urls import re_path
from appbook01.views import user, pretty, admin, account,MsmMessage
from appbook01.views.api import login_view, login_view2
# 3
from appbook01.views.verify import ModelView, user2, Administrator, BookLending

from django.urls import path

urlpatterns = [
    # ############################################前后端分离#######################################################################

    # ######前端用户信息校验########
    path('api/foreground/login/', login_view2.foreground_login, name='foreground'),
    # ########后端用户信息校验######
    path('api/background/login/', login_view2.background_login, name='background'),

    # ########用户注册用户############
    path('api/Signin/', login_view.signin, name='Signin'),
    # #########用户注销##############
    path('logout/', account.logout),
    # ######图片验证#############
    path('api/image/code/', account.image_code2),

    # #########################################后台###############################################
    # #########图书接口###########
    path("api/publishes/", ModelView.PublishView.as_view({"get": "list", "post": "create"})),
    re_path("api/publishes/(?P<pk>\d+)/",
            ModelView.PublishView.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    # #######用户信息接口##########
    path('api/user/', user2.User.as_view({"get": "list", "post": "create"})),
    re_path("api/user/(?P<pk>\d+)/",
            user2.User.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    # ######管理员信息接口##########
    path('api/administrator/', Administrator.Administrator.as_view({"get": "list", "post": "create"})),
    re_path("api/administrator/(?P<pk>\d+)/",
            Administrator.Administrator.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),
    # ######书籍借阅接口##########
    path('api/lending/', BookLending.Administrator.as_view({"get": "list", "post": "create"})),
    re_path("api/lending/(?P<pk>\d+)/",
            BookLending.Administrator.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})),

    # ############################################前后端结合################################################
    # ###############登录##################
    # 登录页面
    path('login/', account.login),
    # 图片验证
    path('image/code/', account.image_code),
    # 短信验证
    path('api/message/code/<str:phone_number>/', MsmMessage.message_code),
    #
    # ###############用户管理##################
    # 用户管理页面
    path('user/list/', user.user_list),
    # 添加用户
    # path('user/add/', user.user_add),
    # 添加用户(UserModelform)
    path('user/model/form/add/', user.user_model_form_add),
    # 删除用户(<int:nid>)设置传递参数类型
    path('user/<int:nid>/delete/', user.user_delete),
    # 编辑用户
    path('user/<int:nid>/edit/', user.user_edit),

    # ###############管理员##################
    # 展示管理员页面
    path('admin/list/', admin.admin_list),
    # 新建管理员
    path('admin/add/', admin.admin_add),
    # 修改管理员
    path('admin/<int:nid>/edit/', admin.admin_edit),
    # 删除管理员
    path('admin/<int:nid>/delete/', admin.admin_delete),
    # 重置密码
    path('admin/<int:nid>/reset/', admin.admin_reset),

    # ###############图书管理##################
    # 展示图书页面
    path('pretty/list/', pretty.pretty_list),
    # 新建图书
    path('pretty/add/', pretty.pretty_add),
    # 编辑图书
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    # 删除图书
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),

]
