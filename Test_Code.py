
import RPi.GPIO as GPIO


from tkinter import *


root = Tk()

var1 = IntVar()

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)


def led_control():

    if var1.get() == 1:

        print('LED IS ON')

        GPIO.output(16, 1)

    else:

        print('LED IS OFF')

        GPIO.output(16, 0)

chk = Checkbutton(root, text="Enable Motor", variable=var1, command=led_control)
chk.pack()


root.mainloop()
