import random
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from app01 import models
from app01.utils.bootstrap import BootStrapModelForm
from app01.utils.pagination import Pagination


class OrderModelForm(BootStrapModelForm):
    class Meta:
        model = models.Order
        # fields = "__all__"
        exclude = ["oid", "admin"]


def order_list(request):
    """页面展示"""
    queryset = models.Order.objects.all().order_by('-id')
    page_object = Pagination(request, queryset)
    form = OrderModelForm()
    context = {
        "form": form,
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(request, 'order_list.html', context)


@csrf_exempt
def order_add(request):
    """添加订单(Ajax请求)"""
    form = OrderModelForm(data=request.POST)
    if form.is_valid():
        # 额外增加不是用户输入的值，自己计算出来的
        # 指定oid的值为：datetime.now().strftime当前时间+random.randint随机字符串
        form.instance.oid = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
        # 当前登录系统的管理员id
        form.instance.admin_id = request.session["info"]["id"]
        # 保存表单数据到数据库
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})


def order_delete(request):
    """删除订单"""
    uid = request.GET.get('uid')
    exists = models.Order.objects.filter(id=uid).exists()
    if not exists:
        return JsonResponse({"status": False, "error": "删除失败，数据不存在"})
    models.Order.objects.filter(id=uid).delete()
    return JsonResponse({"status": True})


def order_detail(request):
    """编辑数据填充"""
    # 方法1
    """    uid = request.GET.get('uid')
        # 得到的row_object是一个对象
        row_object = models.Order.objects.filter(id=uid).first()
        if not row_object:
            return JsonResponse({"status": False, "error": "数据不存在"})
        # 从数据库中获取到一个对象 row_object
        result = {
            "status": True,
            "data": {
                # json序列化不支持对象,
                "title": row_object.title,
                "price": row_object.price,
                "status": row_object.status,
            }
        }
        return JsonResponse(result)
    """
    # 方法2
    uid = request.GET.get('uid')
    # 得到的是一个字典
    row_dict = models.Order.objects.filter(id=uid).values("title", "price", "status").first()
    if not row_dict:
        return JsonResponse({"status": False, "error": "数据不存在"})
    # 从数据库中获取到一个对象 row_object
    result = {
        "status": True,
        "data": row_dict
    }
    return JsonResponse(result)


@csrf_exempt
def order_edit(request):
    """编辑订单保存"""
    uid = request.GET.get("uid")
    row_object = models.Order.objects.filter(id=uid).first()
    if not row_object:
        return JsonResponse({"status": False, "tips": "数据不存在,请刷新重试"})
    form = OrderModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return JsonResponse({"status": True})
    return JsonResponse({"status": False, 'error': form.errors})
