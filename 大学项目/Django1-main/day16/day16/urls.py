from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings

from app01.views import depart, user, pretty, admin, account, task, order, chart, upload, city
from django.urls import path, re_path

urlpatterns = [
    # 配置media
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}, name='media'),
    # ###############部门管理##################
    # 展示部门页面
    path('depart/list/', depart.depart_list),
    # 添加部门
    path('depart/add/', depart.depart_add),
    # 删除部门
    path('depart/delete/', depart.depart_delete),
    # 编辑部门
    path('depart/<int:nid>/edit/', depart.depart_edit),
    # 文件上传
    path('depart/multi/', depart.depart_multi),
    # ###############用户管理##################
    # 展示用户页面
    path('user/list/', user.user_list),
    # 添加用户
    path('user/add/', user.user_add),
    # 添加用户(UserModelform)
    path('user/model/form/add/', user.user_model_form_add),
    # 删除用户(<int:nid>)设置传递参数类型
    path('user/<int:nid>/delete/', user.user_delete),
    # 编辑用户
    path('user/<int:nid>/edit/', user.user_edit),
    # ###############靓号管理##################
    # 展示靓号页面
    path('pretty/list/', pretty.pretty_list),
    # 新建靓号
    path('pretty/add/', pretty.pretty_add),
    # 编辑靓号
    path('pretty/<int:nid>/edit/', pretty.pretty_edit),
    # 删除靓号
    path('pretty/<int:nid>/delete/', pretty.pretty_delete),
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
    # ###############登录##################
    # 登录页面
    path('login/', account.login),
    # 注销
    path('logout/', account.logout),
    # 图片验证
    path('image/code/', account.image_code),
    # ###############ajax测试##################
    # 任务管理页面
    path('task/list/', task.task_list),
    # 发送ajax请求
    path('task/ajax/', task.task_ajax),
    # 表单发送ajax请求
    path('task/add/', task.task_add),
    # ###############ajax模态框应用订单管理##################
    # 任务管理页面
    path('order/list/', order.order_list),
    # 添加
    path('order/add/', order.order_add),
    # 删除数据
    path('order/delete/', order.order_delete),
    # 编辑数据填充
    path('order/detail/', order.order_detail),
    # 编辑保存
    path('order/edit/', order.order_edit),
    # ###############数据统计##################
    # 柱状图展示
    path('chart/list/', chart.chart_list),
    # 柱状图数据构造
    path('chart/bar/', chart.chart_bar),
    # 饼状图数据构造
    path('chart/pie/', chart.chart_pie),
    # 折线图数据构造
    path('chart/line/', chart.chart_line),
    # highcharts示例
    path('chart/highcharts/', chart.highcharts),
    # ###############文件上传##################
    # 上传文件(手工/Form组件)
    path('upload/list/', upload.upload_list),
    # 上传文件及文字
    path('upload/form/', upload.upload_form),
    # 上传文件(ModalForm)全自动建议使用这个
    path('upload/modal/form/', upload.upload_modal_form),
    # 城市列表
    path('city/list/', city.city_list),
    # 新建城市
    path('city/add/', city.city_add),
]
