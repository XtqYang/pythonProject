from django import forms
from django.shortcuts import render, redirect, HttpResponse
from io import BytesIO

from appbook01 import models
from appbook01.utils.bootstrap import BootStrapForm
from appbook01.utils.code import check_code
from appbook01.utils.encrypt import md5


# 手写字段,可以不从数据库中获取
class LoginForm(BootStrapForm):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput,
        # required为True表示不能为空,必填项
        required=True
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

    # 获取用户输入的密码进行md5加密
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def login(request):
    """登录"""
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功,获取到的用户名和密码
        # print(form.cleaned_data)  # 得到{'username': 'xt', 'password': '123','code':xxx}
        # 验证码校验:拿走code的同时会把code去除掉,因为数据库中没有code字段,后面还要使用该对象
        user_input_code = form.cleaned_data.pop('code')
        # 如果不存在结束就是空字符串
        code = request.session.get('image_code', "")
        # upper()将字符串全部变为大写
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {"form": form})
        # 根据用户名去获取对象
        # admin_object = models.Admin.objects.filter(username=form.cleaned_data['username'], password=form.cleaned_data['password']).first()
        # 根据用户名去获取对象,简便方法
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        if not admin_object:
            # 用户名或密码错误
            # 主动往form的字段上显示错误信息
            form.add_error("password", "用c户名或密码错误")
            return render(request, 'login.html', {"form": form})
        # 用户名或密码正确
        # 网站生成随机字符串,写到用户浏览器的cookie中,再写到session中,Django自动完成
        request.session["info"] = {"id": admin_object.id, "name": admin_object.username}
        # 登录成功后重新设置超时时间,因为前面设置了60秒超时,时间太少了,现在设置未7天免登录
        request.session.set_expiry(60 * 60 * 24 * 7)
        return redirect("/admin/list/")
    return render(request, 'login.html', {"form": form})


def logout(request):
    """注销"""
    # 清除当前session
    request.session.clear()
    return redirect('/login/')


def image_code(request):
    """生成图片验证码"""
    # 调用pillow函数,生成图片
    img, code_string = check_code()
    print(code_string)
    # 写到自己的session中,以便后续获取验证码再进行校验
    request.session['image_code'] = code_string
    # 给session设置60秒超时
    request.session.set_expiry(60)
    # BytesIO写入内存(Python3),BytesIO创建一个写入内存中文件
    stream = BytesIO()
    # 将img写入这个内存里
    img.save(stream, 'png')
    # 返回生成图片的内容
    return HttpResponse(stream.getvalue())


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def image_code2(request):
    """生成图片验证码"""
    client_ip = get_client_ip(request)
    print(f"Client IP: {client_ip}")
    # 调用pillow函数,生成图片
    img, code_string = check_code()
    print(code_string)
    # 写到自己的session中,以便后续获取验证码再进行校验
    request.session['image_code'] = code_string
    stream = BytesIO()
    # 将img写入这个内存里
    img.save(stream, 'png')
    # 返回生成图片的内容
    return HttpResponse(stream.getvalue())
