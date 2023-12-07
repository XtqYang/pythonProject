import os

# 要处理的目录路径
dir_path = 'D:/天翼云盘下载/01.海参哥19980全套线下课程等多个文件/01.海参哥19980课程/01参哥高级财商课-价值9980/2'

# 获取目录下的所有文件
file_list = os.listdir(dir_path)

# 遍历文件列表
for file_name in file_list:
    # 去除文件名--后面所有的内容，并加上.mp4
    new_file_name = file_name.split('--')[0] + '.mp4'
    # 构造新的文件路径和文件名
    new_file_path = os.path.join(dir_path, new_file_name)
    old_file_path = os.path.join(dir_path, file_name)
    # 重命名文件
    os.rename(old_file_path, new_file_path)
    # 输出处理结果
    print(f'{file_name} -> {new_file_name}')
