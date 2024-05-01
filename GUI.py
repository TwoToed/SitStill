import tkinter
import detection


def create_gui():

    def start_clicked():
        detection.process_video(detection.video_capture)
    root = tkinter.Tk()
    root.title("Sit Still")
    root.geometry('400x400')
    startbtn = tkinter.Button(root, text="Start Video Capture", fg="red", command=start_clicked)
    startbtn.grid(column=1, row=0)
    root.mainloop()

