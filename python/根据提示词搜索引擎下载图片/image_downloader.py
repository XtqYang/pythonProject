# -*- coding: utf-8 -*-
# author: Yabin Zheng
# Email: sczhengyabin@hotmail.com

from __future__ import print_function

import crawler
import downloader
import sys


def main():
    keywords = "your_search_keywords"  # 设置搜索关键词
    engine = "baidu"  # 设置抓取网站
    max_number = 10  # 设置下载图片数量
    num_threads = 10  # 设置进程数
    timeout = 20  # 设置下载超时
    output = "./download_images"  # 设置输出文件夹
    use_proxy = False  # 设置是否使用代理(默认不使用)

    crawled_urls = crawler.crawl_image_urls(keywords,
                                            engine=engine, max_number=max_number,
                                            use_proxy=use_proxy)
    downloader.download_images(image_urls=crawled_urls, folder_dir=output,
                               max_workers=num_threads, timeout=timeout,
                               use_proxy=use_proxy, file_prefix=engine)

    print("Finished.")


if __name__ == '__main__':
    main()
