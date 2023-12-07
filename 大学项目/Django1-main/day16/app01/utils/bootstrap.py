from django import forms


class BootStrap:
    bootstrap_exclude_fields = []

    # 设置样式,重写__init__方法
    def __init__(self, *args, **kwargs):
        # super()执行父类方法
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件，添加了class="form-control"
        for name, field in self.fields.items():
            # 不添加样式
            if name in self.bootstrap_exclude_fields:
                continue
            # 如果字段中有属性，保留原来的属性，没有才增加
            if field.widget.attrs:
                # 在原有值上新增
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                # 直接赋一个字典
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }


# 针对ModelForm
# 继承BootStrap类
class BootStrapModelForm(BootStrap, forms.ModelForm):
    pass


# 针对Form
# 继承BootStrap类
class BootStrapForm(BootStrap, forms.Form):
    pass
