import os
from PIL import Image


def compress_and_resize_image(input_path, output_folder, compression_level, lossless=False, target_size=None):
    # 判断输入路径是文件还是文件夹
    if os.path.isfile(input_path):
        # 单张图片处理
        process_single_image(input_path, output_folder, compression_level, lossless, target_size)
    elif os.path.isdir(input_path):
        # 文件夹下所有图片处理
        process_images_in_folder(input_path, output_folder, compression_level, lossless, target_size)
    else:
        print("输入路径不存在。")


def process_single_image(input_path, output_folder, compression_level, lossless, target_size):
    # 检查文件是否为图像文件
    if not any(input_path.endswith(ext) for ext in ['.jpg', '.jpeg', '.png']):
        print("输入文件不是图像文件。")
        return

    # 打开图像文件
    image = Image.open(input_path)

    # 调整图像大小
    if target_size:
        image = image.resize(target_size)

    # 创建输出文件夹路径（如果不存在）
    os.makedirs(output_folder, exist_ok=True)

    # 配置压缩选项
    if lossless:
        # 无损压缩
        output_path = os.path.join(output_folder, os.path.basename(input_path))
        image.save(output_path, optimize=True)
    else:
        # 有损压缩
        output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(input_path))[0] + '_compressed.jpg')
        image.save(output_path, optimize=True, quality=compression_level)

    print(f"已处理文件: {input_path}. 输出文件: {output_path}")


def process_images_in_folder(input_folder, output_folder, compression_level, lossless, target_size):
    # 遍历输入文件夹中的所有文件
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        process_single_image(input_path, output_folder, compression_level, lossless, target_size)


# 设置输入路径
input_path = 'D:/浏览器下载/批量图像裁剪/'  # 可以是单张图片的路径或包含图片的文件夹路径

# 设置输出文件夹路径
output_folder = 'C:/Users/21781/Pictures/pixabay/pixabay2.0-压缩0.01/'

# 设置压缩选项
compression_level = 25  # 压缩程度，仅在有损压缩时生效，取值范围为0到100，值越大表示质量越好
lossless = True  # 是否使用无损压缩

# 设置调整大小选项
target_size = (600, 600)  # 目标大小，设置为None表示不调整大小

# 调用压缩和调整大小函数
compress_and_resize_image(input_path, output_folder, compression_level, lossless, target_size)
