import os

from django.shortcuts import render, HttpResponse
from django import forms
from app01.utils.bootstrap import BootStrapForm, BootStrapModelForm
from app01 import models
from django.conf import settings


def upload_list(request):
    if request.method == "GET":
        return render(request, 'upload_list.html')
    # 获取文件对象
    file_object = request.FILES.get("avatar")
    # 根据获取文件名file_object.name
    f = open(file_object.name, mode='wb')
    # 获取文件内容
    for chunk in file_object.chunks():
        f.write(chunk)
    f.close()
    return HttpResponse("....")


class UpForm(BootStrapForm):
    bootstrap_exclude_fields = ['img']

    name = forms.CharField(label="姓名")
    age = forms.IntegerField(label="年龄")
    img = forms.FileField(label="头像")


def upload_form(request):
    title = "Form上传"
    if request.method == "GET":
        form = UpForm()
        return render(request, 'upload_form.html', {"form": form, "title": title})
    # data表单，files文件
    form = UpForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # print(form.cleaned_data)
        # 读取到内容，处理每个字段的数据
        # 读取图片的内容，写入到文件将中并获取文件夹路径
        image_object = form.cleaned_data.get("img")
        # 路径的分隔符再windows和linux中是不一样的，我们就需要使用os拼接路径
        # 静态static:由于用户访问直接获取的是数据库图片路径，不是真正的图片路径(多了一个app01)，我们就把app01换成http://127.0.0.1:8000/
        # db_file_path = os.path.join("static", "img", image_object.name)  # 数据库存储路径
        # file_path = os.path.join("app01", db_file_path)  # 图片存储路径
        # 动态media,绝对路径:settings.MEDIA_ROOT
        media_path = os.path.join(settings.MEDIA_ROOT, image_object.name)  # 数据库存储路径
        # 动态media,相对路径:"media"
        media_path = os.path.join("media", image_object.name)  # 数据库存储路径
        f = open(media_path, mode='wb')
        for chunk in image_object.chunks():
            f.write(chunk)
        f.close()
        # 将图片路径存储到数据库中
        models.Boss.objects.create(
            name=form.cleaned_data['name'],
            age=form.cleaned_data['age'],
            # 存储img为图片路径
            img=media_path,
        )
        return HttpResponse("...")
    return render(request, 'upload_form.html', {"form": form, "title": title})


class UpModelForm(BootStrapModelForm):
    bootstrap_exclude_fields = ['img']

    class Meta:
        model = models.City
        fields = "__all__"


def upload_modal_form(request):
    """ 上传文件和数据（modelForm）"""
    title = "ModelForm上传文件"
    if request.method == "GET":
        form = UpModelForm()
        return render(request, 'upload_form.html', {"form": form, 'title': title})
    form = UpModelForm(data=request.POST, files=request.FILES)
    if form.is_valid():
        # 对于文件：自动保存(路径再创建的数据库中)
        # 字段 + 上传路径写入到数据库
        form.save()
        return HttpResponse("成功")
    return render(request, 'upload_form.html', {"form": form, 'title': title})
