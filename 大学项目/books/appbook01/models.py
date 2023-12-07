from django.db import models


class Lending(models.Model):
    """书籍借阅情况"""
    date = models.CharField(verbose_name="日期", max_length=32)
    username = models.CharField(verbose_name="用户名", max_length=32)
    author = models.CharField(verbose_name="作者", max_length=32)
    BookName = models.CharField(verbose_name="书籍名称", max_length=200)
    mobile = models.CharField(verbose_name="编号", max_length=64, default=0)
    status_choices = (
        (1, "已归还"),
        (0, "未归还")
    )
    give = models.IntegerField(verbose_name="是否归还", choices=status_choices, default=0)


class Admin(models.Model):
    """管理员"""
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)
    ROLE_CHOICES = (
        ("admin", "管理员"),
        ("moderator", "版主"),
    )
    role = models.CharField(verbose_name="角色", max_length=16, choices=ROLE_CHOICES, default="admin")


class UserInfo(models.Model):
    """用户"""
    username = models.CharField(verbose_name="用户名", max_length=16, null=False)
    password = models.CharField(verbose_name="密码", max_length=64, null=False)

    # Student_number = models.CharField(verbose_name="学号", max_length=64)
    # Telephone_number = models.CharField(verbose_name="电话号码", max_length=64)
    # mailbox = models.CharField(verbose_name="邮箱", max_length=64, null=False)
    # age = models.IntegerField(verbose_name="年龄")
    # account = models.DecimalField(verbose_name="账户余额", max_digits=10, decimal_places=2, default=0)
    # create_time = models.DateTimeField(verbose_name="入职时间", default=2022 - 2 - 2)

    # 无约束
    # depart_id = models.BigIntegerField(verbose_name="部门ID")
    # 1.有约束
    #   - to，与那张表关联
    #   - to_field，表中的那一列关联
    # 2.django自动
    #   - 写的depart
    #   - 生成数据列 depart_id
    # 3.部门表被删除
    # ### 3.1 models.CASCADE级联删除，部门删除对应的员工也会删除
    # depart = models.ForeignKey(verbose_name="部门", to="Department", to_field="id", on_delete=models.CASCADE)
    # ### 3.2 置空
    # depart = models.ForeignKey(to="Department", to_field="id", null=True, blank=True, on_delete=models.SET_NULL)

    # 在django中做的约束
    # gender_choices = (
    #     (1, "男"),
    #     (2, "女"),
    # )
    # gender = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

    def __str__(self):
        return self.username


class PrettyNum(models.Model):
    """ 图书表 """
    book_name = models.CharField(verbose_name="书名", max_length=300, default=0)
    Price = models.IntegerField(verbose_name="价格", default=0)
    author = models.CharField(verbose_name="作者", max_length=200, default=0)
    Publishing_house = models.CharField(verbose_name="出版社", max_length=300, default=0)
    mobile = models.CharField(verbose_name="编号(ISBN)", max_length=50, default=0)
    # 想要允许为空 null=True, blank=True
    coverUrl = models.CharField(verbose_name="图片链接", max_length=500, default=1)
    region_choices = (
        ("A", "A区"),
        ("B", "B区"),
        ("C", "C区"),
        ("D", "D区"),
    )
    region = models.CharField(verbose_name="区域", max_length=11, choices=region_choices, default="A")

    # row = models.IntegerField(verbose_name="排", default=0)
    # frame = models.IntegerField(verbose_name="架", default=0)
    #
    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=4)
    status_choices = (
        (1, "已借用"),
        (0, "未借用")
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=0)

    def __str__(self):
        return self.book_name


class Task(models.Model):
    """任务"""
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level_choices = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="任务详细信息")
    user = models.ForeignKey(verbose_name="负责人", to=Admin, on_delete=models.CASCADE)


class Order(models.Model):
    """ 订单 """
    oid = models.CharField(verbose_name="订单号", max_length=64)
    title = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")

    status_choices = (
        (1, "待支付"),
        (2, "已支付"),
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=1)
    # admin_id
    admin = models.ForeignKey(verbose_name="管理员", to="Admin", on_delete=models.CASCADE)
