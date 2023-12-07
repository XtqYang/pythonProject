from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

"""中间件验证是否登录"""


class AuthMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # 0.排除那些不需要登录就能访问的页面
        #   request.path_info 获取当前用户请求的URL /login/
        allowed_paths = ["/login/", "/image/code/", "/api/publishes/", "/api/image/code/",
                         "/api/foreground/login/", "/api/background/login/","/api/foreground/login/",
                         "/api/Signin/", "logout/","/api/publishes/","/api/lending/",]
        if request.path_info in allowed_paths:
            return None

        user = request.user  # 请确保您有一个有效的用户模型和身份验证机制
        if user and user.is_authenticated:
            return None
        else:
            return redirect('/admin/Login')
