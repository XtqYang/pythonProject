from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, HttpResponse
import json
from appbook01.models import UserInfo


# Create your views here.

# @method_decorator(csrf_exempt, name='dispatch')

@csrf_exempt
@require_http_methods(["POST"])
def add_user(request):
    response = {}
    try:
        try:
            idn = UserInfo.objects.last().id
        except:
            idn = 0
        print(request.body.decode())
        data = json.loads(request.body.decode())
        print(data)
        if UserInfo.objects.filter(username=data.get('username')):
            response['msg'] = '用户名已存在'
            response['error_num'] = 2
        else:
            user = UserInfo(id=idn + 1, nickname=data.get('nickname'), username=data.get('username'),
                            password=data.get('password'))
            user.save()
            response['msg'] = 'success\n唯一id: ' + str(idn + 1)
            response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    global data
    response = {}
    try:
        data = json.loads(request.body.decode())
        print(data)
        if UserInfo.objects.filter(username=data.get('username'), password=data.get('password')):
            response['msg'] = 'success'
            response['name'] = data.get('username')
            response['id'] = UserInfo.objects.filter(username=data.get('username')).first().id
            response['error_num'] = 0
        elif not UserInfo.objects.filter(username=data.get('username')):
            response['msg'] = '用户不存在'
            response['error_num'] = 2
        elif UserInfo.objects.filter(username=data.get('username')):
            response['msg'] = '密码错误,请联系管理员'
            response['error_num'] = 3
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    ret = JsonResponse(response)
    if UserInfo.objects.filter(username=data.get('username'), password=data.get('password')):
        ret.set_cookie('username', data.get('username'))
        ret.set_cookie('id', UserInfo.objects.filter(username=data.get('username')).first().id)
    return ret
