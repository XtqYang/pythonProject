from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# appium服务监听地址
server = 'http://localhost:4723/wd/hub'
# app启动参数
desired_caps = {
    "platformName": "Android",
    "platformVersion": "10",
    "deviceName": "SPN-AL00",
    "appPackage": "com.tencent.mm",
    "appActivity": ".ui.LauncherUI",
    # 启动app时不要清除app里原有数据
    "noReset": True,
    # 支持x5内核的自动化配置
    "automationName": "UiAutomator2"
}
# 驱动
driver = webdriver.Remote(server, desired_caps)
wait = WebDriverWait(driver, 30)
# 程序结束不要忘了
driver.quit()
