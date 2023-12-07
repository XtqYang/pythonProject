# 内置模块
import time
# 第三方模块
from django import forms
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
# 自定义模块
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.encrypt import md5

"""添加类"""


class AdminModelForm(BootStrapModelForm):
    # 设置确认密码输入框
    confirm_password = forms.CharField(
        label="确认密码",
        # PasswordInput设置输入的确认密码为不可显示,render_value=True密码输入错误后不会清空密码
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["username", 'password', "confirm_password"]
        # PasswordInput设置输入的密码为不可显示,render_value=True密码输入错误后不会清空密码
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    # 设置钩子
    def clean_password(self):
        # 获取输入的密码
        pwd = self.cleaned_data.get("password")
        # 返回什么,此字段保存到数据库就是什么
        return md5(pwd)

    # 设置钩子
    def clean_confirm_password(self):
        # 获取输入的密码
        pwd = self.cleaned_data.get("password")
        # 获取输入的确认密码
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            # 抛出错误
            raise ValidationError("密码不一致")
        # 返回什么,此字段保存到数据库就是什么
        return confirm


"""编辑类"""


class AdminEditModelForm(BootStrapModelForm):
    class Meta:
        model = models.Admin
        fields = ['username']


"""重置密码类"""


class AdminResetModelForm(BootStrapModelForm):
    # 设置确认密码输入框
    confirm_password = forms.CharField(
        label="确认密码",
        # PasswordInput设置输入的确认密码为不可显示,render_value=True密码输入错误后不会清空密码
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ['password', 'confirm_password']
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    # 设置钩子
    def clean_password(self):
        # 获取输入的密码
        pwd = self.cleaned_data.get("password")
        md5_pwd = md5(pwd)

        # 去数据库校验当前密码和新输入的密码是否一致
        exists = models.Admin.objects.filter(id=self.instance.pk, password=md5_pwd).exists()
        if exists:
            raise ValidationError("不能与以前的密码相同")
        # 返回什么,此字段保存到数据库就是什么
        return md5_pwd

    # 设置钩子
    def clean_confirm_password(self):
        # 获取输入的密码
        pwd = self.cleaned_data.get("password")
        # 获取输入的确认密码
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            # 抛出错误
            raise ValidationError("你输入的密码不一致")
        # 返回什么,此字段保存到数据库就是什么
        return confirm


def admin_list(request):
    """管理员列表"""
    # 检查用户是否已经登录,已登录可以继续向下走,未登录跳转回登录页面
    # 用户发来请求,获取cookie中的随机字符串,拿着随机字符串看看session中有没有
    # info_ = request.session["info"]
    # info = request.session.get("info")
    # # 如果info为空(未登录授权)返回到登录页面,该验证方式繁琐,应该使用中间件验证auth.py
    # if not info:
    #     return redirect('/login/')
    # 搜索
    data_dict = {}
    # 获取get传参数据
    search_data = request.GET.get('q', "")
    # # 只有当value存在值是才执行搜索
    if search_data:
        # 如果存在才往data_dict字典中加入数据json数据
        data_dict["username__contains"] = search_data
    queryset = models.Admin.objects.filter(**data_dict)
    # 分页
    page_object = Pagination(request, queryset)
    context = {
        'queryset': page_object.page_queryset,
        'page_string': page_object.html(),
        "search_data": search_data
    }
    return render(request, 'admin_list.html', context)


def admin_add(request):
    """ 添加管理员 """
    title = "新建管理员"
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'change.html', {'form': form, "title": title})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')

    return render(request, 'change.html', {'form': form, "title": title})


def admin_edit(request, nid):
    """编辑管理员"""
    # 获取当前对象,判断当前nid是否存在
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        # 返回自定义错误页面
        # return render(request, 'error.html',{"msg":"数据不存在"})
        return redirect('/admin/list/')
    title = "编辑管理员"
    if request.method == "GET":
        # 显示编辑信息
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'change.html', {"form": form, "title": title})

    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {"form": form, "title": title})


def admin_delete(request, nid):
    """ 删除管理员 """
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin/list/')


def admin_reset(request, nid):
    """重置密码"""
    # 获取当前对象,判断当前nid是否存在
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin/list/')
    title = "重置密码 - {}".format(row_object.username)

    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'change.html', {"form": form, "title": title})

    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin/list/')
    return render(request, 'change.html', {"form": form, "title": title})
