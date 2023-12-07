from django.http import JsonResponse
import jwt
import json
from appbook01 import models
from django.core.exceptions import ObjectDoesNotExist

SECRET_KEY = ''  # 请设置您的密钥


def generic_login(request, user_model, user_type):
    try:
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')  # 在实际应用中，请使用加密后的密码
        captcha = data.get('captcha')

        if not validate_captcha(request, captcha):
            return JsonResponse({"msg": "验证码错误", "success": False})
        try:
            user_object = user_model.objects.get(username=username, password=password)
        except ObjectDoesNotExist:
            return JsonResponse({"msg": "用户名或密码错误", "success": False})

        payload = {
            'id': user_object.id,
            'username': user_object.username,
            'user_type': user_type
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')
        request.session.set_expiry(60 * 60 * 24 * 7)

        # 根据用户角色返回不同功能
        characters = "普通用户"
        if hasattr(user_object, 'role'):
            if user_object.role == "admin":
                characters = "管理员"
            elif user_object.role == "moderator":
                characters = "版主"
            # ... 你可以根据需要添加更多角色

        return JsonResponse(
            {"msg": "登录成功", "success": True, 'token': token, 'characters': characters,
             'username': user_object.username})

    except json.JSONDecodeError:
        return JsonResponse({"msg": "无效的JSON数据", "success": False}, status=400)


# 前台
def foreground_login(request):
    if request.method == "POST":
        return generic_login(request, models.UserInfo, 'foreground')
    else:
        return JsonResponse({"msg": "请求错误", "success": False}, status=400)


# 后台
def background_login(request):
    if request.method == "POST":
        return generic_login(request, models.Admin, 'background')
    else:
        return JsonResponse({"msg": "请求错误", "success": False}, status=400)


def validate_captcha(request, captcha):
    code = request.session.get('image_code', "")
    print("验证码" + code)
    print("用户验证码" + captcha)
    return code.upper() == captcha.upper()
