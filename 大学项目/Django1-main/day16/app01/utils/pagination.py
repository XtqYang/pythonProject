"""
自定义的分页组件，以后如果想要使用这个分页组件，你需要做如下几件事：

在视图函数中：
    def pretty_list(request):

        # 1.根据自己的情况去筛选自己的数据
        queryset = models.PrettyNum.objects.all()

        # 2.实例化分页对象
        page_object = Pagination(request, queryset)

        context = {
            "queryset": page_object.page_queryset,  # 分完页的数据
            "page_string": page_object.html()       # 生成页码
        }
        return render(request, 'pretty_list.html', context)

在HTML页面中

    {% for obj in queryset %}
        {{obj.xx}}
    {% endfor %}

    <ul class="pagination">
        {{ page_string }}
    </ul>

"""
from django.utils.safestring import mark_safe


class Pagination(object):
    def __init__(self, request, queryset, page_size=10, page_param="page", plus=5):
        """
        :param request: 请求的对象
        :param queryset: 符合条件的数据（根据这个数据给他进行分页处理）
        :param page_size: 每页显示多少条数据
        :param page_param: 在URL中传递的获取分页的参数，例如：/etty/list/?page=12
        :param plus: 显示当前页的 前或后几页（页码）
        """
        from django.http.request import QueryDict
        import copy
        # request.GET默认不可以往url参数中新添值
        query_dict = copy.deepcopy(request.GET)
        # 将request.GET复制(copy)后修改_mutable值为True就可以新添
        query_dict._mutable = True

        self.query_dict = query_dict

        self.page_param = page_param

        # 获取get传参数据，也就是想要的页码，默认设置为1
        page = request.GET.get(page_param, "1")
        # 判断page是否是十进制的数
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        # 想要获取多少条数据
        self.page_size = page_size
        # 获取当前页的开始页码
        self.start = (page - 1) * page_size
        # 获取当前页的结束页码
        self.end = page * page_size
        self.page_queryset = queryset[self.start:self.end]
        # 获取数据库数据总条数
        total_count = queryset.count()
        # 获取总页码数,divmod(*,*)得到这两个数相除的值和余数分别为total_page_count和div
        total_page_count, div = divmod(total_count, page_size)
        if div:
            total_page_count += 1
        self.total_page_count = total_page_count
        self.plus = plus

    # 生成页码方法
    def html(self):
        # 计算出,显示当前页的前5页和后5页
        # 如果数据库数据比较少没有达到11页
        if self.total_page_count <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page_count
        else:
            # 当前页<5时
            if self.page <= self.plus:
                start_page = 1
                end_page = self.plus * 2
            else:
                # 当前页>5时
                if self.page + self.plus >= self.total_page_count:
                    # 先乘后减
                    start_page = self.total_page_count - 2 * self.plus
                    end_page = self.total_page_count
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus
        # 后台生成页码
        page_str_list = []
        # 新填参数，键是self.page_param，值是数组类型
        self.query_dict.setlist(self.page_param, [1])
        # 首页
        # self.query_dict.urlencode中包含收参数
        prev = '<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)
        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
            page_str_list.append(prev)
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
            page_str_list.append(prev)
        # 循环多少次前端展示多少个页码,range前取后不取后面加一
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            # 如果是当前页,在当前页加一个样式
            if i == self.page:
                # format(i,i)往前面字符串中{}添加为i
                els = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(),i)
            else:
                els = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(els)
        # 下一页
        if self.page < self.total_page_count:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
            page_str_list.append(prev)
        else:
            self.query_dict.setlist(self.page_param, [self.total_page_count])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
            page_str_list.append(prev)
        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page_count])
        prev = '<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode())
        page_str_list.append(prev)
        # 跳转
        # 搜索需要结合Ajax请求来做，当前这个无法实现
        search_string = """
            <li>
                <form style="float: left;margin-left: -1px" method="get">
                    <input name="page"
                           style="position: relative;float:left;display: inline-block;width: 80px;border-radius: 0;"
                           type="text" class="form-control" placeholder="页码">
                    <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
                </form>
            </li>
            """
        page_str_list.append(search_string)
        page_string = mark_safe("".join(page_str_list))
        return page_string
