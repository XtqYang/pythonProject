from lxml import etree

# 读取1.html文件并创建一个Element对象
with open("../1.html", "r", encoding="utf-8") as file:
    html_content = file.read()
    root = etree.HTML(html_content)

xpath_expression = "//a[@class='woo-nxt']/@pdir"
href_elements = root.xpath(xpath_expression)
print(href_elements)
