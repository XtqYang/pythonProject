from django.shortcuts import render, redirect
from appbook01 import models
from appbook01.utils.pagination import Pagination
from appbook01.utils.form import UserModelForm, PrettyModelForm, PrettyEditModelForm


# 将字符串标记为安全的
# from django.utils.safestring import mark_safe

# ################################# 靓号 #################################

def pretty_list(request):
    """图书列表"""

    # 筛选filter(id=12)等于12,filter(id__gt)=12大于12,filter(id__gte=12)大于等于12,filter(id__lt=12)小于12,filter(id__lte=12)小于等于12的所有数据
    # 筛选filter(mobile="999")等于999的所有数据,filter(mobile_startswith="999"以999开头的所有数据,filter(mobile_endswith="999"以999结尾的所有数据,filter(mobile_contains="999"包含999的所有数据
    """搜索功能"""  # ###
    # q = models.PrettyNum.objects.filter(mobile="142343243", id=2)
    # print(q)
    # data_dict = {"mobile": "142343243", "id": "2"}
    # 以对象方式传递，想要在变量前加上**
    # q2 = models.PrettyNum.objects.filter(**data_dict)
    # print(q2)
    data_dict = {}
    # 获取get传参数据
    search_data = request.GET.get('q', "")
    # # 只有当value存在值是才执行搜索
    if search_data:
        # 如果存在才往data_dict字典中加入数据json数据
        data_dict["mobile__contains"] = search_data
    """分页功能"""  # ###
    # [*:*]显示符合条件的第*到*条数据
    queryset = models.PrettyNum.objects.filter(**data_dict).order_by("-level")
    page_object = Pagination(request, queryset)
    context = {
        "search_data": search_data,  # 搜索显示搜索值
        'queryset': page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 页码
    }
    return render(request, 'pretty_list.html', context)


"""新建图书类"""


def pretty_add(request):
    """添加图书"""
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {"form": form})
    # 获取提交的post数据
    form = PrettyModelForm(data=request.POST)
    # 保存数据
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    return render(request, 'pretty_add.html', {"form": form})


"""编辑图书类"""


def pretty_edit(request, nid):
    """编辑图书"""
    row_object = models.PrettyNum.objects.filter(id=nid).first()

    if request.method == "GET":
        form = PrettyEditModelForm(instance=row_object)
        # 根据nid，获取他的数据对象
        return render(request, 'pretty_edit.html', {"form": form})

    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    # 如果form为true执行保存
    if form.is_valid():
        form.save()
        return redirect('/pretty/list/')
    # 否则执行，返回错误对象
    return render(request, 'pretty_edit.html', {"form": form})


"""删除图书类"""


def pretty_delete(request, nid):
    """删除图书"""
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list/')
