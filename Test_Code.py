
import pygame
from tkinter import *

root = Tk()

var1 = IntVar()


def play_audio(event):
    if var1.get() == 1:
        pygame.mixer.init()
        pygame.mixer.music.load("TEST1.wav")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    else:

        print('AUDIO IS OFF')


audio_button = Button(root, text="Play Audio!", variable=var1)
audio_button.bind("<ButtonPress-1>", play_audio)
audio_button.pack()

root.mainloop()
