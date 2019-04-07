from tkinter import *
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial=GPIO.LOW)

##hardware
red = 8
yellow = 16
green = 22

## gui definitions ##
win = Tk()
win.title("LED Toggler")

## event functions ##
def toggleYellow():
    GPIO.output(yellow, GPIO.HIGH)
    GPIO.output(red, GPIO.LOW)
    GPIO.output(green, GPIO.LOW)
        
def toggleRed():
    GPIO.output(yellow, GPIO.LOW)
    GPIO.output(red, GPIO.HIGH)
    GPIO.output(green, GPIO.LOW)
        
def toggleGreen():
    GPIO.output(yellow, GPIO.LOW)
    GPIO.output(red, GPIO.LOW)
    GPIO.output(green, GPIO.HIGH)
    
##def exitProgram():
    ##win.quit()

## widgets ##
R1 = Radiobutton(win, text="Red LED", command=toggleRed, value=1)
R1.grid(row=5,column=0)

R2 = Radiobutton(win, text="Yellow LED", command=toggleYellow, value=2)
R2.grid(row=5,column=1)

R3 = Radiobutton(win, text="Green LED", command=toggleGreen, value =3)
R3.grid(row=5,column=2)
    
exitButton=Button(win, text='Exit', command=quit, height=1, width=6)
exitButton.grid(row=6, column=2)


win.mainloop()