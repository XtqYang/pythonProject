
## scrapy框架
![](C:/Users/21781/AppData/Local/Temp/204136k0npe3szsx36epqd.png)
![img.png](img.png)
![](C:/Users/21781/AppData/Local/Temp/303f581b771ccebfaa3108a30dc56bd2a0b20498451acbec3dc1c71dc8648aa0.png)
## 1.创建game项目

scrapy startproject duitang_com

## 2.cd game进入game创建爬虫xiao限定爬虫域名抓取范围4399.com

scrapy genspider tianya_all duitang.com

## 3.运行项目

scrapy crawl duitang_all
