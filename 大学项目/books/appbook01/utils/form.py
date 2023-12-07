from appbook01 import models
from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from appbook01.utils.bootstrap import BootStrapModelForm
# 将字符串标记为安全的
from django.utils.safestring import mark_safe


class UserModelForm(BootStrapModelForm):
    # 重定义字段name,定制验证name规则
    name = forms.CharField(min_length=2, label='用户名')

    # 默认具有校验表单是否为空
    class Meta:
        model = models.UserInfo
        fields = "__all__"
        # 设置样式 widgets = {"name": forms.TextInput(attrs={"class": "form-control"}) }


"""添加"""


class PrettyModelForm(BootStrapModelForm):
    # 验证方式一(字段加正则),语法:字段 = forms.CharField(验证规则)
    # mobile = forms.CharField(
    #     label="手机号",
    #     # 正则表达式匹配，后面还可以加多个
    #     validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式错误'), ],
    # )
    # 验证方式2(钩子方法),语法: clean_字段
    def clean_mobile(self):
        # 获取用户传入的数据(mobile)图书编号号
        txt_mobile = self.cleaned_data["mobile"]
        # exists()可以验证数据是否存在,返回true或false
        exists = models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("编号已存在")
        # 如果传入编号长度小于10个字符就抛出错误，raise ValidationError("错误提示")
        if len(txt_mobile) < 7:
            raise ValidationError("格式错误")
        # 如果通过就返回当前值
        return txt_mobile

    # 你要显示哪些字段
    class Meta:
        model = models.PrettyNum
        # 所有字段
        fields = "__all__"
        # fields = ["book_name", "Price", "author", "Publishing_house", 'mobile', 'coverUrl','region','row','frame','level','status']
        # 排除level字段
        # exclude = ['level']
        # fields 是把models 中的字段拿过来，你用什么就拿什么
        # fields = ["mobile", 'price', 'author', 'region', 'row', 'frame', 'level', 'status', 'gender']


"""编辑"""


class PrettyEditModelForm(BootStrapModelForm):
    # 重定义字段mobile，设置为不可改
    # mobile = forms.CharField(disabled=True, label="手机号")
    # 验证方式一(字段加正则),语法:字段 = forms.CharField(验证规则)
    mobile = forms.CharField(
        label="图书编号",
        # 正则表达式匹配，后面还可以加多个
        # validators=[RegexValidator(r'^1[3-9]\d{9}$', '编号号格式错误'), ],
    )

    # 你要显示哪些字段a
    class Meta:
        model = models.PrettyNum
        fields = "__all__"
        # fields = ["book_name", "Price", "author", "Publishing_house", 'mobile', 'coverUrl', 'region', 'row', 'frame',
        #           'level', 'status']

    # 验证方式2(钩子方法),语法: clean_字段
    def clean_mobile(self):
        # 获取用户传入的数据(mobile)手机号
        txt_mobile = self.cleaned_data["mobile"]
        # instance.pk就是当前编辑那一行的id它的id
        # print(self.instance.pk)

        # exclude不等于,filter等于,意思是排除它本身手机号以外,检查其它的手机号是否存在新的手机号
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")

        # 如果传入手机号长度小于10个字符就抛出错误，raise ValidationError("错误提示")
        if len(txt_mobile) <10:
            raise ValidationError("格式错误")
        # 如果通过就返回当前值
        return txt_mobile
