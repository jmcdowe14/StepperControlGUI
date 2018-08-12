import RPi.GPIO as GPIO, time

from Tkinter import *

import sys

root = Tk()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)

GPIO.setup(18, GPIO.OUT)

GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(16, 100)

titleLabel = Label(root, text="Stepper Motor Controller", bg="green", fg="white")
pinSetup = Label(root, text="Pin are Set as [Enable] = 22, [DIR] = 18. [STP] = 16")
statusLabel = Label(root, text="Controller is set to: {}".format(MotorStatus))

enableMotor = Checkbutton(root, text="Enable Motor")
forwardButton = Button(root, text="Forward")
backwardButton = Button(root, text="Backward")
stopButton = Button(root, text="STOP")


titleLabel.pack()
pinSetup.pack()

forwardButton.bind("<forwardButton>", SpinForward)
forwardButton.grid(row=0, column=0)

backwardButton.grid(row=0, column=1)
backwardButton.bind("<backwardButton>", SpinBackward)

stopButton.grid(row=0, column=3)
stopButton.bind("<stopButton>", Shutdown)


enableMotor.grid(columnspan=2)

MotorStatus = 'text'

def ControlStatus():

    global MotorStatus

    if enableMotor == True:
        MotorStatus = 'ON'

    else:
        MotorStatus = 'OFF'

def SpinMotor(dire):
    p.ChangeFrequency(100)

    GPIO.out(18,dire)

    p.start(1)

    time.sleep(0.01)

    return True

def SpinForward(event):

    GPIO.out(22, 1)

    SpinMotor(True)

def SpinBackward(event):

    GPIO.out(22, 0)

    SpinMotor(False)

def Shutdown(event):

    p.stop()

    GPIO.cleanup()

while True:



root.mainloop()
