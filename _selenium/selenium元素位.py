from selenium import webdriver
from selenium.webdriver.common.by import By

# 创建浏览器操作对象
path = 'chromedriver.exe'
# 选择浏览器内核加入对象
browser = webdriver.Chrome(path)
# 访问网站
url = 'https://www.baidu.com/'
browser.get(url)
# 基于属性元素定位
button = browser.find_element(By.ID, "su")
button2 = browser.find_element(By.CLASS_NAME, "s_ipt")
print(button)
print(button2)
# 基于文本的定位-局限性:只能定位链接
button = browser.find_element(By.PARTIAL_LINK_TEXT, '新')  # 模糊匹配
button2 = browser.find_element(By.LINK_TEXT, '新闻')  # 精准匹配
print(button)
print(button2)
# 基于表达式的定位
button = browser.find_element(By.CSS_SELECTOR, "#su")
print(button)
# 基于xpath的定位,xpath是文档查询语言,天生兼容HTML,很好根据文档层级进行定位，支持灵活的语法函数
button = browser.find_elements(By.XPATH, '//*[@id="su"]')
print(button)
