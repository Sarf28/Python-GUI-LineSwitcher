from tkinter import *
import tkinter.font
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
GPIO.output(12, GPIO.LOW)
GPIO.setup(10, GPIO.OUT)
GPIO.output(10, GPIO.LOW)
GPIO.setup(8, GPIO.OUT)
GPIO.output(8, GPIO.LOW)

win = Tk()

myfont = tkinter.font.Font(family = 'Helvetica', size = 36, weight = 'bold')

myfont1 = tkinter.font.Font(family = 'Helvetica', size = 28, weight = 'bold')

def led1ON():
    print("Gateway1 button pressed")
    if GPIO.input(12):
        GPIO.output(12,GPIO.LOW)
        ledButton["text"]="TURN ON"
    else:
        GPIO.output(12,GPIO.HIGH)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        ledButton["text"]="TURN OFF"
        ledButton2["text"]="TURN ON"
        ledButton3["text"]="TURN ON"

def led2ON():
    print("Gateway2 button pressed")
    if GPIO.input(10):
        GPIO.output(10,GPIO.LOW)
        ledButton2["text"]="TURN ON"
    else:
        GPIO.output(12,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
        ledButton["text"]="TURN ON"
        ledButton2["text"]="TURN OFF"
        ledButton3["text"]="TURN ON"

def led3ON():
    print("Gateway3 button pressed")
    if GPIO.input(8):
        GPIO.output(8,GPIO.LOW)
        ledButton3["text"]="TURN ON"
    else:
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        ledButton["text"]="TURN ON"
        ledButton2["text"]="TURN ON"
        ledButton3["text"]="TURN OFF"
        

def exitProgram():
    print("Exit button pressed")
    GPIO.cleanup()
    win.destroy()

win.title("Line Switcher")
win.geometry('800x480')

exitButton  = Button(win, text = "Exit", font = myfont, command = exitProgram, height =2 , width = 6) 
exitButton.pack(side = BOTTOM)

ledButton = Button(win, text = "TURN ON", font = myfont, command = led1ON, height = 2, width =8 )
ledButton.pack(side = LEFT)

ledButton2 = tkinter.Button(win, text = "TURN ON", font = myfont, command = led2ON, height = 2, width = 8)
ledButton2.pack(side = RIGHT)

ledButton3 = tkinter.Button(win, text = "TURN ON", font = myfont, command = led3ON, height = 2, width = 8)
ledButton3.pack()
ledButton3.place(x = 277, y = 120)

text1 = Text(win, height = 1, width = 9, font = myfont1)
text1.pack()
text1.place(x = 20, y = 250)
text1.insert(END, "Gateway 1")

text2 = Text(win, height = 1, width = 9, font = myfont1)
text2.pack()
text2.place(x = 580, y = 250)
text2.insert(END, "Gateway 3")

text3 = Text(win, height = 1, width = 9, font = myfont1)
text3.pack()
text3.place(x = 300, y = 250)
text3.insert(END, "Gateway 2")


mainloop()


      