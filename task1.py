#! python3
""" 
Create a binary converter.
Recall that binary is a system of counting based on powers of 2.
00000001 = 1
00000010 = 2
00001110 = 14

Create a converter that will convert binary to decimal or decimal to
binary using the interface shown in task1.png.  Use the shell that
has been started in task1.py
This is an incomplete program.  You will need to add onto it, 
but you should not change any of the commands that are already 
here

Use assignment_test.py to test your functions
"""

import tkinter as tk
from tkinter import *

win = tk.Tk()
win.title("Fortnite lol")

s = []
for x in range(8):
    s.append(IntVar())
    s[x].set(0)

def binary_to_decimal(binary):
    # binary is a tuple of length 8
    # return value is an integer decimal
    decimal = 0
    for x in range(8):
        if s[x].get() == 1:
            decimal += 2**x 
    return decimal 

def decimal_to_binary(decimal):
    # decimal is an integer value
    # binary is a tuple of length 8 that contains 1's and 0's
    nums = [128, 64, 32, 16, 8, 4, 2, 1]
    binary = []
    for x in range(8):
        if decimal >= nums[x]:
            decimal -= nums[x]
            binary.append(1)
        else:
            binary.append(0)
    return binary

def get_binary():
    # function should read the entry widget and generate an integer
    # this integer will be used as an input parameter for decimal to binary and the result updated
    # in the 8 checkboxes
    decimal = int(entry.get())
    binary = decimal_to_binary(decimal)
    binary.reverse()
    for x in range(8):
        if binary[x] == 1:
            c[x].select()
        else:
            c[x].deselect()

def get_decimal():
    # function should read the checkboxes and generate a tuple called binary of length 8 that has 1's and 0's
    # this tuple will be used as an input parameter for binary_to_decimal and the result updated
    # in the entry box
    binary = []
    for x in range(8):
        binary.append(s[x].get())
    decimal = binary_to_decimal(binary)
    entry.delete(0, tk.END)
    entry.insert(0, decimal)

frame1 = Frame(win)
frame2 = Frame(win)
label = Label(win, text = "Binary / Decimal Converter!")
b1 = Button(master = frame2, text = "Convert to Binary", command = get_binary)
b2 = Button(master = frame2, text = "Convert to Decimal", command = get_decimal)
c = []
for x in range(8):
    c.append(Checkbutton(master = frame1, variable = s[x]))
entry = Entry(win)

label.pack()
frame1.pack()
frame2.pack()
b1.pack(side = LEFT)
b2.pack(side = LEFT)
for x in range (8):
    c[x].pack(side = RIGHT)
entry.pack()

win.mainloop()