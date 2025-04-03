import priority
import to_do
import sqlite3
import tkinter
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import *

class MonthView():

    # CREATE MAIN gui window
    root = Tk()
    root.title("Week View")

    #(root, height, width, bd, bg, ..) https://www.geeksforgeeks.org/python-tkinter-canvas-widget/
    # verticalLine1 = root.create_line(186, 0, 186, 1000, width=5)
    # verticalLine2 = root.create_line(372, 0, 372, 1000, width=5)
    # verticalLine3 = root.create_line(558, 0, 558, 1000, width=5)
    # verticalLine4 = root.create_line(744, 0, 744, 1000, width=5)
    # verticalLine5 = root.create_line(930, 0, 930, 1000, width=5)
    # verticalLine6 = root.create_line(1110, 0, 1110, 1000, width=5)
    #https://www.tutorialspoint.com/how-to-set-a-certain-number-of-rows-and-columns-of-a-tkinter-grid
    #https://pythonlobby.com/python-grid-grid-geometry-manager-in-tkinter-grid-layout/
    label1 = Label(root, text='Label1', font=("Calibri, 15"))
    label1.grid(column=0, row=0)
    label2 = Label(root, text='Label2', font=("Calibri, 15"))
    label2.grid(column=1, row=1)
    label = Label(root, text='Label2', font=("Calibri, 15"))
    label.grid(column=1000, row=2, rowspan = 5)
    w = Label(root, text="I'm in 3rd Column", bg="red", fg="white")
    w.grid(column=3)
    w = Label(root, text="I've columnspan of 3", bg="light green", fg="white")
    w.grid(columnspan=3)
    w = Label(root, text="I've ipadx of 5", bg="yellow", fg="red")
    w.grid(ipadx=100)
    # horizontalLine1 = root.create_line(0, 50, 1300, 50, width=5)
#https://www.geeksforgeeks.org/python-tkinter-label/

    # label1 = Label(root, text='Label1', font=("Calibri, 15"))
    # label1.grid(column=0, row=0)
    #https: // www.geeksforgeeks.org / python - tkinter - scrollbar /

    # create and config and form frame

# implement a scroll thingy later https://pythonguides.com/python-tkinter-scrollbar/

    # run tkinter main loop
    #https://stackoverflow.com/questions/7966119/display-fullscreen-mode-on-tkinter
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    root.mainloop()