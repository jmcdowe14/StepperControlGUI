import RPi.GPIO as GPIO, time
from tkinter import *

import sys

root = Tk()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)

GPIO.setup(18, GPIO.OUT)

p = GPIO.PWM(16, 100)

titleLabel = Label(root, text="Stepper Motor Controller", bg="green", fg="white")
titleLabel.pack()


def SpinMotor(dire):
    p.ChangeFrequency(100)

    GPIO.out(18,dire)

    p.start(1)

    time.sleep(0.01)

    return True

while True:

    dir_input = raw_input("Enter your dir: ")

    if dir_input == "f":

        SpinMotor(True)

    elif dir_input == "b":

        SpinMotor(False)

    elif dir_input == "s":

        p.stop()

        dir_input = ""

    elif dir_input == "shutdown":

        p.stop()

        GPIO.cleanup()

        break

root.mainloop()
