import os
from Tkinter import *

root = Tk()

def play_morning(event):
    os.system('mpg321 audio_1.mp3 &')
    print('AUDIO IS PLAYING')

def play_hello(event):
    os.system('mpg321 audio_2.mp3 &')
    print('AUDIO IS PLAYING')

def play_night(event):
    os.system('mpg321 audio_3.mp3 &')
    print('AUDIO IS PLAYING')

audioButton1 = Button(root, text="GOOD MORNING!")
audioButton1.bind("<ButtonPress-1>", play_morning)
audioButton1.pack()

audioButton2 = Button(root, text="HELLO CATS!")
audioButton2.bind("<ButtonPress-1>", play_hello)
audioButton2.pack()

audioButton3 = Button(root, text="GOOD NIGHT KITTENS!")
audioButton3.bind("<ButtonPress-1>", play_night)
audioButton3.pack()

root.mainloop()
