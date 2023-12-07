from django.http import HttpResponse

from appbook01.utils.ShortMessage import sms


def message_code(request, phone_number):
    """生成短信验证码"""
    code_string = sms(phone_number)
    # 将短信验证码存储在session中，以便后续进行校验
    request.session['message_code'] = code_string
    # 设置session的超时时间，例如300秒
    request.session.set_expiry(300)
    return HttpResponse("短信验证码已发送")  # 或者其他的响应内容
