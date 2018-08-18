import RPi.GPIO as GPIO
import os
import time

from tkinter import *

root = Tk()

var1 = IntVar()

var2 = IntVar()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)

GPIO.setup(18, GPIO.OUT)

GPIO.setup(22, GPIO.OUT)

GPIO.setup(32, GPIO.OUT)

GPIO.output(22, 1)

p = GPIO.PWM(16, 100)

def spin_motor(dire):
    p.ChangeFrequency(100)
    GPIO.output(18, dire)
    p.start(1)
    time.sleep(0.01)

def relayswitch_on(event):

    if var2.get() ==1:
        GPIO.output(32, 0)
    else:
        print('Relay Control Not Active!')

def relayswitch_off(event):
    if var2.get() == 1:
        GPIO.output(32, 1)
    else:
        print('Relay Control Not Active!')

def play_morning(event):
    os.system('mpg321 audio_1.wma &')
    print('AUDIO IS PLAYING')

def play_hello(event):
    os.system('mpg321 audio_2.wma &')
    print('AUDIO IS PLAYING')

def play_night(event):
    os.system('mpg321 audio_3.wma &')
    print('AUDIO IS PLAYING')

def spin_forward(event):
    if var1.get() == 1:
        GPIO.output(22, 0)
        spin_motor(1)
    else:
        print('MOTOR NOT ENABLED!')

def spin_backward(event):
    if var1.get() == 1:
        GPIO.output(22, 0)
        spin_motor(0)
    else:
        print('MOTOR NOT ENABLED!')

def shutdown(event):
    if var1.get() == 1:
        GPIO.output(22, 1)
        p.stop()
    else:
        print('MOTOR NOT ENABLED!')

chk1 = Checkbutton(root, text="Enable Motor", variable=var1)
chk1.pack()

chk2 = Checkbutton(root, text="Enable Relay", variable=var2)
chk2.pack()

forwardButton = Button(root, text="Forward")
forwardButton.bind("<ButtonPress-1>", spin_forward)
forwardButton.bind("<ButtonRelease-1>", shutdown)
forwardButton.pack()

backwardButton = Button(root, text="Backward")
backwardButton.bind("<ButtonPress-1>", spin_backward)
backwardButton.bind("<ButtonRelease-1>", shutdown)
backwardButton.pack()

stopButton = Button(root, text="STOP")
stopButton.bind("<ButtonPress-1>", shutdown)
stopButton.pack()

relayON = Button(root, text="Relay ON")
relayON.bind("<ButtonPress-1>", relayswitch_on)
relayON.pack()

relayOFF = Button(root, text="Relay OFF")
relayOFF.bind("<ButtonPress-1>", relayswitch_off)
relayOFF.pack()

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

GPIO.cleanup()