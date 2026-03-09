from pytubefix import YouTube
import tkinter as tk
from tkinter import filedialog

def download_vid(url,path):
    try:
        yt=YouTube(url)
        stream=yt.streams.filter(progressive=True,file_extension="mp4")
        high_res=stream.get_highest_resolution()
        high_res.download(output_path=path)
        print("done")
    except Exception as e:
        print(e)
def open_file():
    folder=filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
        return folder

if __name__=="__main__":
    root =tk.Tk()
    root.withdraw()

    vid_url=input("Enter url: ")
    save_dir=open_file()

    if not save_dir:
        
        print("ivalid loc")
    else:
        print("started sir")
        download_vid(vid_url,save_dir)