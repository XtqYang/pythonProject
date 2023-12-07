import re

# 从文件中读取HTML文本
file_path = "1.html"
with open(file_path, 'r', encoding='utf-8') as file:
    html_text = file.read()

# 定义匹配正则表达式
pattern = r'www\.zhihu\.com/pin/\d+'
# pattern = r'zhuanlan.zhihu.com/p/\d+"'
# pattern = r'[\u4e00-\u9fa5，。；！？：“”‘’【】/（）—…「」MINI《》" "、|&!@#$%^&^&*()\d+<br>.]{10,}'


# 使用正则表达式进行匹配
matches = re.findall(pattern, html_text)

# 输出满足条件的链接
for match in matches:
    print(match)
