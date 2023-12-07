#!/usr/bin/env python
# 项目管理文件，启动项目，创建app，数据管理
"""Django's command-line utility for administrative tasks."""
import os
import sys


# 1.创建项目     django-admin startproject 项目名
# 2.创建app     python manage.py startapp app名称
# 3.生成数据库表  python manage.py makemigrations  python manage.py migrate
# 启动项目 python manage.py runserver
def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
