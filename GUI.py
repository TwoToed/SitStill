import tkinter
import detection
from datetime import datetime

start_time = datetime.now().strftime("%H:%M:%S")
def create_gui():

    def start_clicked():
        print("hello")
        detection.process_video(detection.video_capture)
    root = tkinter.Tk()
    root.title("Sit Still")
    root.geometry('500x500')
    startlabel = tkinter.Label(root, text = "Start Time: " + start_time, fg = "red")
    startbtn = tkinter.Button(root, text="Start Video Capture", fg="red", command=start_clicked)
    startbtn.grid(column=0, row=0)
    startlabel.grid(column=0, row=1)
    root.mainloop()

