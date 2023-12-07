from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def share_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    # path是你自己的chrome浏览器的文件路径
    path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome()
    return browser


browser = share_browser()
url = 'https://www.baidu.com'
browser.get(url)
browser.save_screenshot('baidu.png')