from lxml import etree

# // 查找所有子孙节点，不考虑层级关系
# / 查找子接点

# xpath解析
# (1) 本地文件  etree.parse
# (2) 服务器响应数据 response.read().decode('utf-8')   etree.HTML()
tree = etree.parse('D:\code\pythonProject\wj\html\hello.html')
li_list = tree.xpath('//body//ul/li/text()')  # text()获取标签内容
print(li_list)
print(len(li_list))  # 判断列表长度
# 查找所有有id属性的li标签
li_list = tree.xpath('//ul/li[@id]/text()')
print(li_list)
# text()获取标签某个id内容
li_list = tree.xpath('//ul/li[@id="l1"]/text()')
print(li_list)
# 查找id为l1的li标签的class的属性值
li_list = tree.xpath('//ul/li[@id="l1"]/@class')
print(li_list)

# 模糊查询
# 查找id里面包含l的li标签内容
li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(li_list)
# 查询id值以2开头的li标签内容
li_list = tree.xpath('//ul/li[starts-with(@id,"2")]/text()')
print(li_list)
# 逻辑运算
# 查询id为l1和class为c1的内容
li_list = tree.xpath('//ul/li[@id="l1" and @class="c1"]/text()')
print(li_list)
# | 或
li_list = tree.xpath('//ul/li[@id="l1"]/text() | //ul/li[@id="l2"]/text()')
print(li_list)
