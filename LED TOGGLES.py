from tkinter import *
import tkinter.font                                           # Libraries used for the task
from gpiozero import LED as RedL
from gpiozero import LED as YellowL
from gpiozero import LED as GreenL
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

RedLed = RedL(14)                   # Setting the pins for the led's 
YellowLed = YellowL(15)
GreenLed = GreenL(18)

win = Tk() #creating a window.
win.title("LED Toggler") #creating  the title of the window.
winFont = tkinter.font.Font(family = 'Cambria', size = 14, weight = "bold") # defining custom font

def RedLedToggle(): # Code for red led

    if RedLed.is_lit:
        RedLed.off()
        RedLedButton["text"] = "Turn Red LED on"

    else:

        YellowLed.off()
        GreenLed.off()
        RedLed.on()
        RedLedButton["text"] = "Turn Red LED off"


def YellowLedToggle():

    if YellowLed.is_lit: # Code for yellow led

        YellowLed.off()
        YellowLedButton["text"] = "Turn Yellow LED on"

    else:

        RedLed.off()
        GreenLed.off()
        YellowLed.on()
        YellowLedButton["text"] = "Turn Yellow LED off"


def GreenLedToggle(): # Code for green led

    if GreenLed.is_lit:

        GreenLed.off()
        GreenLedButton["text"] = "Turn Green LED on"

    else:

        RedLed.off()
        YellowLed.off()
        GreenLed.on()
        GreenLedButton["text"] = "Turn Green LED off"

def close(): # Exit command's code

    GPIO.cleanup()
    RedLed.off()
    YellowLed.off()
    GreenLed.off()
    win.destroy()

    # Code for creating the Radio buttons
    
RedLedButton = Radiobutton(win, text = 'Turn Red LED on', font  = winFont, command = RedLedToggle, bg = 'red', height = 1, width = 24)  
RedLedButton.grid(row=0, column=1)

YellowLedButton = Radiobutton(win, text = 'Turn Yellow LED on', font  = winFont, command = YellowLedToggle, bg = 'yellow', height = 1, width = 24)  
YellowLedButton.grid(row=1, column=1)

GreenLedButton = Radiobutton(win, text = 'Turn Green LED on', font  = winFont, command = GreenLedToggle, bg = 'green', height = 1, width = 24)  
GreenLedButton.grid(row=2, column=1)

exitButton = Radiobutton(win, text = 'Exit', font  = winFont, command = close, bg = 'black', height = 1, width = 24)  
exitButton.grid(row=3, column=1)

win.protocol("WM_DELETE_WINDOW", close)

win.mainloop()
