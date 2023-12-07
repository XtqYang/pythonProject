from selenium.webdriver.common.by import By
from selenium import webdriver
import time
# 停止更新
path = 'phantomjs.exe'
browser = webdriver.PhantomJS(path)
url = 'https://www.baidu.com'
browser.get(url)
time.sleep(2)
# 获取文本框的对象
input = browser.find_element(By.ID, "kw")
# 在文本框中输入周杰伦
input.send_keys('周杰伦')
time.sleep(2)
# 获取百度一下的按钮
button = browser.find_element(By.ID, "su")
# 点击按钮
button.click()
time.sleep(2)
# 滑动到底部
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)
time.sleep(3)
# 获取下一页的按钮
next = browser.find_element(By.XPATH, '//a[@class="n"]')
# 拍照
browser.save_screenshot('baidu.png')
# 点击下一页
next.click()
time.sleep(3)
# 回到上一页
browser.back()
time.sleep(3)
# 回去
browser.forward()
time.sleep(3)
# 退出
browser.quit()
