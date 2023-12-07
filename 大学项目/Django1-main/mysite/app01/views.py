from django.shortcuts import render, HttpResponse, redirect
# Django内部提供ORM框架，开发操作数据库更简单
from app01.models import Department, UserInfo


# 重要，视图函数

def index(request):
    return HttpResponse("欢迎使用")


# render实现返回给用户html页面
# 如果需要优先到根目录的templates文件下找html文件需要配置"DIRS"为:[os.path.join(BASE_DIR,'templates')],
# 默认情况下去app目录下的templates文件下找html文件(根据app的注册顺序，逐一的去templates目录中找)
def user_list(request):
    return render(request, "user_list.html")


def user_add(request):
    return render(request, "user_add.html")


def user_tpl(request):
    name = "小明"
    # 数组
    roles = ["管理员", "CEO", "保安"]
    # 字典
    user_info = {"name": "小明", "lisha": 10000, "role": "CTO"}
    # 数组里面套字典
    data_list = [
        {"name": "小明", "lisha": 10000, "role": "CTO"},
        {"name": "小芳", "lisha": 10000, "role": "CTO"},
        {"name": "小东", "lisha": 10000, "role": "CTO"}
    ]
    return render(request, "tpl.html", {"n1": name, "n2": roles, "n3": user_info, "n4": data_list})


def news(req):
    import requests
    # 定义一些新闻(字典或列表)，网络请求联通
    res = requests.get("http://www.chinaunicom.cn/api/article/NewsByIndex/2/2022/07/news")
    data_list = res.json()
    print(data_list)

    return render(req, 'news.html', {"news_list": data_list})


def something(request):
    # 1.获取请求方式GET/POST
    print(request.method)
    # 2.获取URL上传递的值
    print(request.GET)
    # 3.获取请求头中提交数据
    print(request.POST)
    # request是一个对象，封装了用户通过浏览器发送过来的所有请求相关的数据
    # 4.[响应]return HttpResponse("返回内容")
    # 5.[响应]return render(request,"something.html",{"title":"来了"})
    # 6.[响应]让浏览器重定向到其他页面
    return redirect("https:www.baidu.com")


def login(request):
    # 如果是get请求
    if request.method == "GET":
        return render(request, "login.html")
    # 如果是post请求，获取用户提交的数据
    # print(request.POST)
    username = request.POST.get("user")
    password = request.POST.get("pwd")
    if username == "root" and password == "123":
        # return HttpResponse("登录成功")
        return redirect("https:www.baidu.com")
    # return HttpResponse("登录失败")
    return render(request, "login.html", {"error_msg": "登录失败用户名或密码错误"})


def orm(request):
    # 测试ORM表中数据
    # create()新建,all()所有,update()更新
    # filter()筛选,delete()删除,first()QuerySet对象转换
    #####1.新建#####
    # UserInfo.objects.create(name="小明", password="123", age=12)
    # UserInfo.objects.create(name="小东", password="423", age=14)
    # Department.objects.create(title="销售部")
    # Department.objects.create(title="IT部")
    #####2.删除#####
    # filter()加筛选条件,delete()删除
    # UserInfo.objects.filter(id=2).delete()
    #####3.获取所有数据#####
    # 3.1得到的数据是QuerySet类型
    # data_list = UserInfo.objects.all()
    # 使用循环获取QuerySet对象中的所有数据
    # for obj in data_list:
    #     print(obj.id, obj.name, obj.password, obj.age)
    # 3.2得到一行数据，得到的依然是QuerySet对象，后面加上first()得到的就是那一行数据
    # row_obj = UserInfo.objects.filter(id=1).first()
    # print(row_obj.id, row_obj.name, row_obj.password, row_obj.age)
    #####4.更新数据#####
    # UserInfo.objects.filter(name="小明").update(password=666)
    return HttpResponse('成功')


def info_list(request):
    # 获取数据库中所有用户信息
    data_list = UserInfo.objects.all()
    return render(request, "info_list.html", {"data_list": data_list})


def info_add(request):
    if request.method == "GET":
        return render(request, "info_add.html")
    # 获取用户提交数据
    user = request.POST.get("user")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    # 添加到数据库
    UserInfo.objects.create(name=user, password=pwd, age=age)
    return redirect("http://127.0.0.1:8000/info/list/")

def info_delete(request):
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("http://127.0.0.1:8000/info/list/")
