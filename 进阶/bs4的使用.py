from bs4 import BeautifulSoup

# 通过bs4解析本地文件
# 默认打开的编码格式是GBK,打开需要指定编码
soup = BeautifulSoup(open('bs4.html', encoding='utf-8'), 'lxml')

# 根据标签查找节点,找到的是的一个符合条件的数据集
print(soup.a)
# # attrs获取标签的属性和属性值
print(soup.a.attrs)

# bs4的一些函数
# find 返回第一个符合条件的数据
print(soup.find('a'))
print(soup.find('a', title="a2"))  # 通过条件找到对应的标签
print(soup.find('a', class_="a1"))  # class是python用到的关键词，用到class值找对应标签对象需要加下划线_ 即是class标签又不能作为关键词
# find_all
print(soup.find_all('a'))  # 返回一个列表，并且返回了所有a标签
print(soup.find_all(['a', 'span']))  # 如果想获取多个标签的数据，那么需要在find_all的参数中添加的是列表数据
print(soup.find_all('li', limit=2))  # limit的作用是查找前几个数据集
# select(推荐) 返回一个列表，并且返回多个数据
print(soup.select('a'))
print(soup.select('.a1'))  # 可以通过.代表class，我们把这种操作叫做类选择器
print(soup.select('#l1'))  # 可以通过#代表id查找标签数据

# 属性选择器--通过属性来寻找对应的标签
print(soup.select('li[id]'))  # 查找li标签中有id的标签
print(soup.select('li[id="l2"]'))  # 查找li标签中id为l2的标签

# 层级选择器
# 后代选择器，找到div下面的li
print(soup.select('div li'))
# 子代选择器，某标签的第一级子标签，在很多计算机编程语言中，如果不加空格不会输出内容，但在bs4中不会报错
print(soup.select('div > ul > li'))
# 组合选择器
print(soup.select('a,span'))

# 节点信息
# 获取节点的内容
obj = soup.select('#d1')[0]
print(obj.string)  # 如果标签对象中只有内容那么String和get_text()都可以使用
print(obj.get_text())  # 如果标签对象中除了内容还有标签，那么String就获取不到数据，而get_text()是可以获取数据,推荐使用使用get_text()
# 节点的属性
obj = soup.select('#p1')[0]
print(obj.name)  # 获取id为p1的标签名字
print(obj.attrs)  # 将属性值以一个字典返回
# 获取节点属性,3种方式
obj = soup.select('#p1')[0]
print(obj.attrs.get('class'))
print(obj.get('class'))
print(obj['class'])
