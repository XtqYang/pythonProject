from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm, PrettyModelForm, PrettyEditModelForm
# 将字符串标记为安全的
# from django.utils.safestring import mark_safe
# ################################# 用户 #################################


def user_list(request):
    """ 用户管理 """

    # 获取所有用户列表 [obj,obj,obj]
    queryset = models.UserInfo.objects.all()
    # 增加分页
    page_object = Pagination(request, queryset, page_size=2)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
    }
    """
    # 用Python的语法获取数据
    for obj in queryset:
        print(obj.id, obj.name, obj.account, obj.create_time.strftime("%Y-%m-%d"), obj.gender, obj.get_gender_display(), obj.depart_id, obj.depart.title)
        # print(obj.name, obj.depart_id)
        # obj.depart_id  # 获取数据库中存储的那个字段值
        # obj.depart.title  # 根据id自动去关联的表中获取哪一行数据depart对象。
    """
    return render(request, 'user_list.html', context)


def user_add(request):
    """ 添加用户（原始方式） """

    if request.method == "GET":
        context = {
            'gender_choices': models.UserInfo.gender_choices,
            "depart_list": models.Department.objects.all()
        }
        return render(request, 'user_add.html', context)

    # 获取用户提交的数据
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    age = request.POST.get('age')
    account = request.POST.get('ac')
    ctime = request.POST.get('ctime')
    gender = request.POST.get('gd')
    depart_id = request.POST.get('dp')

    # 添加到数据库中
    models.UserInfo.objects.create(name=user, password=pwd, age=age,
                                   account=account, create_time=ctime,
                                   gender=gender, depart_id=depart_id)

    # 返回到用户列表页面
    return redirect("/user/list/")


def user_model_form_add(request):
    """ 添加用户（ModelForm版本）"""
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_model_form_add.html', {"form": form})

    # 用户POST提交数据，数据校验。
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        # 如果数据合法，保存到数据库
        # {'name': '123', 'password': '123', 'age': 11, 'account': Decimal('0'), 'create_time': datetime.datetime(2011, 11, 11, 0, 0, tzinfo=<UTC>), 'gender': 1, 'depart': <Department: IT运维部门>}
        # print(form.cleaned_data)
        # models.UserInfo.objects.create(..)
        form.save()
        return redirect('/user/list/')

    # 校验失败（在页面上显示错误信息）
    return render(request, 'user_model_form_add.html', {"form": form})


def user_delete(request, nid):
    """删除用户"""
    # 包含在URL中的{{ obj.id }数据，使用nid接收这个数据,然后使用delete()删除
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')


def user_edit(request, nid):
    """编辑用户"""
    # 获取这个nid用户所有数据对象，使用row_object.字段,来获取数据
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        # 将你的id获取出来的数据以html展示，如：
        # <tr>
        #     <th><label for="id_name">用户名:</label></th>
        #     <td>
        #       <input type="text" name="name" value="xtq" class="form-control" placeholder="用户名" required id="id_name">
        #     </td>
        #   </tr>
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {"form": form})
    # 校验表单
    form = UserModelForm(data=request.POST, instance=row_object)
    # 如果表单正确执行
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要再用户输入以外增加一点值使用form.instance.字段名 = 值
        form.save()
        return redirect('/user/list/')
    # 表单错误携带错误数据返回
    return render(request, 'user_edit.html', {"form": form})
