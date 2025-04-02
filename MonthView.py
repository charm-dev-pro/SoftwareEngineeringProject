import priority
import to_do
import sqlite3
import tkinter
import tkinter as tk
import tkinter.messagebox


conn = sqlite3.connect('SEProject1.db')
cur = conn.cursor()
from tkinter import *

class MonthView():

    # CREATE MAIN gui window
    root = tk.Tk()

    root.geometry("1200x900")
    root.title("Registration form")
    canvas.create_line(15, 25, 200, 25, width=5)
    canvas.pack()
    # set gui background color
    root.configure(background="white")


    # create and config and form frame
    form_frame = tk.Frame(root, padx=20, pady=20)
    form_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)



    # run tkinter main loop
    root.mainloop()