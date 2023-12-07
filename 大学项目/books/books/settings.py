import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-4u$agsgx)&8c7f#j9$k_cx_cby11u01m!o4*$928am4&*%h8oq"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    'appbook01.apps.Appbook01Config',
    'rest_framework',
    'corsheaders',  # CORS解决跨域问题

]
# 中间件
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS跨域中间件
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'appbook01.middleware.auth.AuthMiddleware'
]

ROOT_URLCONF = "books.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'templates']
        ,
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "books.wsgi.application"

# 服务器数据库
# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # 默认
#         'NAME': 'mybook',  # 连接的数据库  #一定要存在的数据库名
#         'HOST': '5ju9367358.oicp.vip',  # mysql的ip地址
#         'PORT': 45928,  # mysql的端口
#         'USER': 'root',  # mysql的用户名
#         'PASSWORD': 'hy064872'  # mysql的密码
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认
        'NAME': 'mybook',  # 连接的数据库  #一定要存在的数据库名
        'HOST': '127.0.0.1',  # mysql的ip地址
        'PORT': 3306,  # mysql的端口
        'USER': 'root',  # mysql的用户名
        'PASSWORD': 'hy064872'  # mysql的密码
    }
}
# 云数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # 默认
#         'NAME': 'mybook',  # 连接的数据库  #一定要存在的数据库名
#         'HOST': 'mybook.mysql.database.azure.com',  # mysql的ip地址
#         'PORT': 3306,  # mysql的端口
#         'USER': 'xtq',  # mysql的用户名
#         'PASSWORD': 'Hy064872#'  # mysql的密码
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
MEDIA_URL = '/media/'  # 用于指定url路径
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 使用数据库存储会话数据
SESSION_ENGINE = 'django.contrib.sessions.backends.db'

# # 设置为True时，只有在HTTPS连接下才会发送会话Cookie
# SESSION_COOKIE_SECURE = True

# SESSION_COOKIE_DOMAIN = {'.yvedu.free.idcfengye.com', '8.130.51.216', '117.136.62.44', '127.0.0.1'}
#
# # 允许跨域请求
# CORS_ALLOW_ALL_ORIGINS = True
# # 指定域名
# CORS_ALLOWED_ORIGINS = [
#     "http://8.130.51.216",
#     "http://117.136.62.44",
#     "http://127.0.0.1",
#     "https://5ju9367358.oicp.vip"
# ]
