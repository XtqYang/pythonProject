from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from appbook01.models import UserInfo


# 获取最后一个用户的ID
def get_last_user_id():
    try:
        last_user = UserInfo.objects.last()
        return last_user.id if last_user else 0
    except Exception as e:
        print(f"获取最后一个用户ID时出错: {str(e)}")
        return 0


# 用于处理用户注册请求
@csrf_exempt
@require_http_methods(["POST"])
def signin(request):
    try:
        data = json.loads(request.body.decode())
        response = create_user_response(data)
    except Exception as e:
        response = create_error_response(str(e), 1)
    return JsonResponse(response)


# 用于处理用户登录请求
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    try:
        data = json.loads(request.body.decode())
        response = create_login_response(data)
        #         response['msg'] = '登录成功'
        #         response['name'] = data['username']
        #         response['id'] = user.id
        #         response['error_num'] = 0
        if response['error_num'] == 0:
            cookies = {
                'username': data['username'],
                'id': response['id']
            }
            set_cookies(cookies, response)
    except Exception as e:
        response = create_error_response(str(e), 1)
    ret = JsonResponse(response)
    return ret


# 用于创建用户注册响应
def create_user_response(data):
    response = {}
    idn = get_last_user_id()
    if UserInfo.objects.filter(username=data['username']):
        response['msg'] = '用户名已存在'
        response['error_num'] = 2
    else:
        user = UserInfo(id=idn + 1, username=data['username'], password=data['password'])
        user.save()
        response['msg'] = f'注册成功\n唯一ID: {idn + 1}'
        response['error_num'] = 0
    return response


# 用于创建用户登录响应
def create_login_response(data):
    response = {}
    user = UserInfo.objects.filter(username=data['username'], password=data['password']).first()
    if user:
        response['msg'] = '登录成功'
        response['name'] = data['username']
        response['id'] = user.id
        response['error_num'] = 0
        print("登录成功")
        print(user.id)
    elif not UserInfo.objects.filter(username=data['username']):
        response['msg'] = '用户不存在'
        response['error_num'] = 2
        print("用户不存在")

    else:
        response['msg'] = '密码错误，请联系管理员'
        response['error_num'] = 3
        print("密码错误")
    return response


# 用于创建错误响应
def create_error_response(msg, error_num):
    return {'msg': msg, 'error_num': error_num}


# 设置Cookie
def set_cookies(cookies, response):
    for cookie_name, cookie_value in cookies.items():
        response.set_cookie(cookie_name, cookie_value)
