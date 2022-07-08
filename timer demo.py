from playsound import playsound
from tkinter import *
import time

Hour, Min, Secs = 0,0,0

Sec = int(input("Timer Limit In Seconds : "))


if Sec > 59:
    Min, Secs = Secs//60, Secs%60
if Min > 59:
    Hour, Min = Min//60, Min%60

Time = str(Hour) + " hours " + str(Min) + " min " + str(Sec) + " sec"


root = Tk()
root.geometry("450x200")
root.title("Timer")
root.resizable(False, False)
root.config(bg = "#303030")

Timer = Label(root,
    text = "Timer For " + Time,
    font = ("Candara",25),
    bg = "#303030",
    fg = "#C8C8C8")
Timer.place(relx=0, rely=0, relheight = 0.3, relwidth = 1.0)

def countdown(Sec):
    while Sec:
        mins, secs = divmod(Sec, 60)
        hour, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        Sec -= 1
countdown(Sec)

Time = Label(root,
    text = "Tatata",
    font = ("Candara",45),
    bg = "#303030",
    fg = "#C8C8C8")
Time.place(relx = 0, rely=0.3, relheight = 0.5, relwidth = 1.0)

root.mainloop()

'''print("Timer for 15 second starts now!")
time.sleep(15)
print("Timer ends!")
playsound("D:\\Recording.wav")
'''
