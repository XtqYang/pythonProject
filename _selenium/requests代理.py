import requests
from lxml import etree
url = 'https://www.nsu.edu.cn/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'
}
data = {
    'wd': 'ip'
}
proxy = {
    'http': '61.164.39.68:53281'
}
response = requests.get(url=url, params=data, headers=headers,)
