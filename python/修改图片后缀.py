import os

path = 'C:/Users/21781/Pictures/pixabay'  # 指定文件夹路径

for filename in os.listdir(path):
    if filename.endswith('.png'):  # 判断文件是否以 .png 结尾
        new_filename = os.path.splitext(filename)[0] + '.jpg'  # 获取新的文件名
        os.rename(os.path.join(path, filename), os.path.join(path, new_filename))  # 修改文件名