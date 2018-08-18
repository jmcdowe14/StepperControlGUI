
import pygame
from tkinter import *

pygame.mixer.init()
sound1 = pygame.mixer.Sound('TEST1.mp3')

root = Tk()

def play_audio(event):
    sound1.play()
    print('AUDIO IS PLAYING')

audioButton = Button(root, text="Play Audio!")
audioButton.bind("<ButtonPress-1>", play_audio)
audioButton.pack()

root.mainloop()
