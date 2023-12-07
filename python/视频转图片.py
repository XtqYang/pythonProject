import os
from tkinter import Tk, Button, Listbox, Label
from tkinter.filedialog import askopenfilenames
from tkinter.ttk import Progressbar
from moviepy.editor import VideoFileClip
from PIL import Image


def convert_videos_to_images():
    selected_videos = list(selected_videos_listbox.get(0, "end"))
    if not selected_videos:
        print("请选择至少一个视频")
        return

    for video_path in selected_videos:
        try:
            video_name = os.path.basename(video_path)
            video_name_without_ext = os.path.splitext(video_name)[0]
            output_folder = f"{video_name_without_ext}_picture"
            os.makedirs(output_folder, exist_ok=True)

            clip = VideoFileClip(video_path)
            total_frames = int(clip.duration * clip.fps)
            progress_bar["maximum"] = total_frames

            for frame_num, frame in enumerate(clip.iter_frames()):
                image = Image.fromarray(frame)
                image.save(f"{output_folder}/{frame_num}.png")
                progress_bar["value"] = frame_num + 1
                progress_label["text"] = f"进度：{frame_num+1}/{total_frames}"
                window.update()

            print(f"{video_name}的图片已生成")
        except Exception as e:
            print(f"处理视频时出错：{str(e)}")


def add_videos():
    video_paths = askopenfilenames(filetypes=[("视频文件", "*.mp4")])
    selected_videos_listbox.insert("end", *video_paths)


def delete_selected_video():
    selected_indices = selected_videos_listbox.curselection()
    if not selected_indices:
        return

    for index in reversed(selected_indices):
        selected_videos_listbox.delete(index)


def preview_selected_video():
    selected_index = selected_videos_listbox.curselection()
    if not selected_index:
        return

    video_path = selected_videos_listbox.get(selected_index)
    os.startfile(video_path)


window = Tk()
window.title("视频转图片")
window.geometry("500x400")

selected_videos_label = Label(window, text="已选视频：")
selected_videos_label.pack()

selected_videos_listbox = Listbox(window, selectmode="extended")
selected_videos_listbox.pack()

add_videos_button = Button(window, text="添加视频", command=add_videos)
add_videos_button.pack()

delete_video_button = Button(window, text="删除视频", command=delete_selected_video)
delete_video_button.pack()

preview_video_button = Button(window, text="预览视频", command=preview_selected_video)
preview_video_button.pack()

convert_button = Button(window, text="转换为图片", command=convert_videos_to_images)
convert_button.pack()

progress_label = Label(window, text="进度：0/0")
progress_label.pack()

progress_bar = Progressbar(window, orient="horizontal", length=200, mode="determinate")
progress_bar.pack()

window.mainloop()
