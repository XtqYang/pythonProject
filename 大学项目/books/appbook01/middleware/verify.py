from rest_framework.authentication import SessionAuthentication
from rest_framework.exceptions import AuthenticationFailed

from appbook01.models import Admin


def valid_cookie(cookie_value):
    try:
        # 查询数据库，检查是否存在匹配的会话记录
        session = Admin.objects.get(cookie_value=cookie_value)
        # 检查会话关联的用户是否为活动用户
        if session.user.is_active:
            return True
    except Admin.DoesNotExist:
        pass

    return False


class CustomCookieAuthentication(SessionAuthentication):
    def authenticate(self, request):
        print("验证")
        # 调用父类的 authenticate 方法以使用Session验证
        user_auth_tuple = super().authenticate(request)

        if user_auth_tuple is not None:
            user, auth = user_auth_tuple
            # 在这里添加你的Cookie验证逻辑
            # 例如，验证某个特定的Cookie是否存在且合法
            cookie_value = request.COOKIES.get('sessionid')
            print(cookie_value)
            if cookie_value is not None:
                # 进行合法性验证，比如检查cookie_value是否有效
                if valid_cookie(cookie_value):
                    return user, auth
            else:
                raise AuthenticationFailed('Invalid Cookie')

        return None
