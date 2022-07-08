# Stole This One From Net And Changed A Bit
# Might need to use some audio file in this one or just comment it

import time
from playsound import playsound

def Countdown(Sec):
    while Sec:
        mins, secs = divmod(Sec, 60)
        hour, mins = divmod(mins, 60)
        timer = '{:02d}:{:02d}:{:02d}'.format(hour, mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        Sec -= 1

Sec = int(input("Enter time in seconds : "))
print("Timer for " + str(Sec) + " second starts now!")
Countdown(Sec)
print("Timer ends!")
playsound("D:\\Recording.wav")

#Basically karna yhi hai par thoda sa achcha dikhne k lie tkinter p chal rha tha