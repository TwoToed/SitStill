import tkinter
import detection
from datetime import datetime
import time

def start_clicked():
    print("hello")
    detection.set_time_track(time.time())
    detection.process_video()
def create_gui():
    def update_labels():
        at_com_label.config(text="at com time in min: " + "{:.2f}".format(detection.get_at_com() / 60))
        not_at_com_label.config(text="not at com time in min: " + "{:.2f}".format(detection.get_not_at_com() / 60))

    root = tkinter.Tk()
    root.title("Sit Still")
    root.geometry('500x500')
    #labels
    startbtn = tkinter.Button(root, text="Start Video Capture", fg="red", command=start_clicked)
    updatebtn = tkinter.Button(root, text="Check Timing", fg="red", command=update_labels)
    at_com_label = tkinter.Label(root, text="at com time in min: 0")
    not_at_com_label = tkinter.Label(root, text="not at com time in min: 0")
    startbtn.grid(column=0, row=0)
    updatebtn.grid(column=0, row=1)
    at_com_label.grid(column=0, row=2)
    not_at_com_label.grid(column=0, row=3)
    root.mainloop()

