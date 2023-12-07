import json
from django import forms
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination
from app01 import models


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        # 所有字段
        fields = "__all__"
        widgets = {
            # "detail": forms.Textarea,
            "detail": forms.TextInput
        }


def task_list(request):
    """任务列表"""
    # 去数据库获取所有任务,根据id倒叙排列
    queryset = models.Task.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)

    form = TaskModelForm()

    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }

    return render(request, "task_list.html", context)


# @csrf_exempt免除POST发送的scrf认证
@csrf_exempt
def task_ajax(request):
    print(request.GET)
    print(request.POST)
    data_dict = {"status": True, "data": [11, 22, 33, 44]}
    # 向用户返回的数据,发送前需要序列化obj为JSON格式的str。
    return HttpResponse(json.dumps(data_dict))
    # return JsonResponse(data_dict)


@csrf_exempt
def task_add(request):
    # 对用户发送过来的数据进行校验
    form = TaskModelForm(data=request.POST)
    # 验证成功
    if form.is_valid():
        form.save()
        data_dict = {"status": True}
        return HttpResponse(json.dumps(data_dict))
    # 验证失败
    data_dict = {"status": False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
