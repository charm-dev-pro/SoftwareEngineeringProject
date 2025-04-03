import priority
import to_do
import sqlite3
import tkinter
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
from tkinter import *

conn = sqlite3.connect('SEProject1.db')
cur = conn.cursor()


class MonthView():

    # CREATE MAIN gui window
    root = tk.Tk()
    canvas = Canvas(root, bg="white", height = 1500, width = 1300)
    root.title("Week View")
    #(root, height, width, bd, bg, ..) https://www.geeksforgeeks.org/python-tkinter-canvas-widget/
    verticalLine1 = canvas.create_line(186, 0, 186, 1000, width=5)
    verticalLine2 = canvas.create_line(372, 0, 372, 1000, width=5)
    verticalLine3 = canvas.create_line(558, 0, 558, 1000, width=5)
    verticalLine4 = canvas.create_line(744, 0, 744, 1000, width=5)
    verticalLine5 = canvas.create_line(930, 0, 930, 1000, width=5)
    verticalLine6 = canvas.create_line(1110, 0, 1110, 1000, width=5)

    horizontalLine1 = canvas.create_line(0, 50, 1300, 50, width=5)
#https://www.geeksforgeeks.org/python-tkinter-label/
    text_var = tk.StringVar()
    text_var.set("Hello, World!")

    #https: // www.geeksforgeeks.org / python - tkinter - scrollbar /

    # create and config and form frame
    form_frame = tk.Frame(root, padx=20, pady=20)
    form_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
    text_box = Text(root,height=13,width=32,font=12)

# implement a scroll thingy later https://pythonguides.com/python-tkinter-scrollbar/

    # run tkinter main loop
    canvas.pack()
    root.mainloop()