import urllib.request
import urllib.parse
from lxml import etree
from bs4 import BeautifulSoup

url = 'https://www.starbucks.com.cn/menu/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
}
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

soup = BeautifulSoup(content, 'lxml')
# //div[@class="wrapper fluid margin page-menu-list"]//strong/text()
name_list = soup.select('div[class="wrapper fluid margin page-menu-list"] strong')
for name in name_list:
    print(name.string)
