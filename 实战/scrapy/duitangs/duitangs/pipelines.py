import os
import requests
import scrapy
from scrapy.pipelines.images import ImagesPipeline


#
# import os
# import scrapy
# from scrapy.pipelines.images import ImagesPipeline
#
#
# class ImgsPipeline(ImagesPipeline):
#     """
#     类说明：自定义的专用于图片下载的管道类
#     """
#
#     def get_media_requests(self, item, info):
#         """
#         函数说明：根据图片地址进行图片数据的请求
#         :param item:
#         :param info:
#         :return:
#         """
#         print(item['img_src'])
#         try:
#             # 这里因为获取的是二进制数据，所以不需要 callback回调请求
#             yield scrapy.Request(item['img_src'])
#         except Exception as e:
#             self.logger.error(f"Error while making request for {item['img_src']}. Error: {e}")
#
#     def file_path(self, request, response=None, info=None, *, item=None):
#         """
#         函数说明：指定图片存储的路径
#         :param request:
#         :param response:
#         :param info:
#         :param item:
#         :return:
#         """
#         try:
#             imgname = os.path.basename(request.url)  # 获取URL的最后一部分作为图片名称
#             return imgname
#         except Exception as e:
#             self.logger.error(f"Error while determining file path for {request.url}. Error: {e}")
#             return "unknown.jpg"
#
#     def item_completed(self, results, item, info):
#         return item  # 返回给下一个即将被执行的管道类


class DuitangsPipeline:
    # 创建目录
    # def open_spider(self, spider):
    #     self.img_dir = './meinvtupian'
    #     if not os.path.exists(self.img_dir):
    #         os.makedirs(self.img_dir)

    def process_item(self, item, spider):
        img_url = item["img_src"]
        print(img_url)
        # 下载图片
        response = requests.get(img_url)
        # 使用URL的最后部分作为文件名
        img_filename = os.path.join(item["path"], os.path.basename(img_url))
        print("下载路径：" + item["path"])
        # 保存图片到文件
        with open(img_filename, 'wb') as f:
            f.write(response.content)

    def close_spider(self, spider):
        print("下载完成")
