import tkinter as tk
from tkinter import ttk
from tkinter import *

# this is the function called when the button is clicked


def calibrateClicked():
    print('clicked')


# this is a function to get the user input from the text input box
def getInputBoxValue():
    userInput = bellNum.get()
    return userInput


root = Tk()

# This is the section of code which creates the main window
root.geometry('880x590')
root.configure(background='#F0F8FF')
root.title('Calibration')


# This is the section of code which creates the a label
Label(root, text='Follow the on screen instructions for calibration',
      bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=263, y=76)


# This is the section of code which creates a button
Button(root, text='Press to start calibration', bg='#F0F8FF', font=(
    'arial', 12, 'normal'), command=calibrateClicked).place(x=343, y=256)


# This is the section of code which creates a text input box
bellNum = Entry(root)
bellNum.place(x=383, y=186)


# This is the section of code which creates the a label
Label(root, text='Enter the number of bells below then press the button to continue',
      bg='#F0F8FF', font=('arial', 12, 'normal')).place(x=233, y=126)


root.mainloop()
