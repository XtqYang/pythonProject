import os
import random
import cv2
from tkinter import *
from tkinter import ttk, filedialog

# 获取文件夹中所有图片的路径
def get_image_paths(folder_path):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    image_paths = []
    for file_name in os.listdir(folder_path):
        extension = os.path.splitext(file_name)[1]
        if extension.lower() in image_extensions:
            image_paths.append(os.path.join(folder_path, file_name))
    return image_paths

# 生成随机顺序的图片列表
def get_random_image_sequence(image_paths):
    random.shuffle(image_paths)
    return image_paths

# 将图片序列组合成视频
def create_video(image_sequence, video_name, fps):
    frame_size = cv2.imread(image_sequence[0]).shape[1::-1]
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video_writer = cv2.VideoWriter(video_name, fourcc, fps, frame_size)
    for image_path in image_sequence:
        image = cv2.imread(image_path)
        video_writer.write(image)
    video_writer.release()

# tkinter GUI
class App:
    def __init__(self, master):
        self.master = master
        self.master.title("图片转视频")
        self.master.geometry("400x150")

        # 文件夹路径选择按钮
        self.folder_path_label = Label(self.master, text="请选择文件夹：")
        self.folder_path_label.grid(row=0, column=0)
        self.folder_path_entry = Entry(self.master)
        self.folder_path_entry.grid(row=0, column=1)
        self.folder_path_button = Button(self.master, text="选择文件夹", command=self.select_folder_path)
        self.folder_path_button.grid(row=0, column=2)

        # 视频帧率输入框
        self.fps_label = Label(self.master, text="请输入视频帧率：")
        self.fps_label.grid(row=1, column=0)
        self.fps_entry = Entry(self.master)
        self.fps_entry.grid(row=1, column=1)

        # 进度条
        self.progress_bar = ttk.Progressbar(self.master, orient=HORIZONTAL, length=200, mode='determinate')
        self.progress_bar.grid(row=2, column=0, columnspan=3)

        # 开始转换按钮
        self.start_button = Button(self.master, text="开始转换", command=self.start_conversion)
        self.start_button.grid(row=3, column=1)

    # 选择文件夹路径
    def select_folder_path(self):
        folder_path = filedialog.askdirectory(title="选择文件夹")
        self.folder_path_entry.delete(0, END)
        self.folder_path_entry.insert(0, folder_path)

    # 开始转换
    def start_conversion(self):
        folder_path = self.folder_path_entry.get()
        fps = int(self.fps_entry.get())
        image_paths = get_image_paths(folder_path)
        image_sequence = get_random_image_sequence(image_paths)
        video_name = os.path.join(folder_path, "D:/code/pythonProject/python/output.mp4")
        create_video(image_sequence, video_name, fps)
        self.progress_bar['value'] = 100

root = Tk()
app = App(root)
root.mainloop()
