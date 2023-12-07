import json
import jsonpath

# $ 	文档根元素
# @ 	当前元素
# .或[] 匹配下级元素
# N/A 	匹配上级元素，JsonPath不支持此操作符
# .. 	递归匹配所有子元素
# * 	通配符，匹配下级元素
# N/A 	匹配属性，JsonPath不支持此操作符
# [] 	下标运算符，根据索引获取元素，XPath索引从1开始，JsonPath索引从0开始
# ` 	[,]
# [start:end:step] 	数据切片操作，XPath不支持
# ?() 	过滤表达式
# ) 	脚本表达式，使用底层脚本引擎，XPath不支持
# N/A 	分组，JsonPath不支持
obj = json.load(open('D:\code\pythonProject\wj\json\KFC_2.json', 'r', encoding='utf-8'))
# 所有KFC地址,可以通过改变[]中的下标获取指定的地址
author_list = jsonpath.jsonpath(obj, '$.Table1[*].storeName')
print(author_list)
# 所有地址
author_list = jsonpath.jsonpath(obj, '$..storeName')
print(author_list)
# Table1下面的所有元素
tag_list = jsonpath.jsonpath(obj, '$.Table1.*')
print(tag_list)
# Table1下面所有东西的城市
price_list = jsonpath.jsonpath(obj, '$.Table1..cityName')
print(price_list)
# Table1的第1个
rownum = jsonpath.jsonpath(obj, '$..Table1[0]')
print(rownum)
# Table1最后1个
rownum = jsonpath.jsonpath(obj, '$..Table1[(@.length-1)]')
print(rownum)
# Table1前2个
# rownum = jsonpath.jsonpath(obj, '$..Table1[0,1]') 或
rownum = jsonpath.jsonpath(obj, '$..Table1[:2]')
print(rownum)
# 条件过滤需要在()的前面添加一个?
# 过滤出所有包含pro的Table1
rownum = jsonpath.jsonpath(obj, '$..Table1[?(@.pro)]')
print(rownum)
# Table1中大于13的rownum
rownum = jsonpath.jsonpath(obj, '$..Table1[?(@.rownum>13)]')
print(rownum)