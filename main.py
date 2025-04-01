import calendar
import priority
import to_do
import sqlite3
import tkinter
import tkinter as tk
import tkinter.messagebox

conn = sqlite3.connect('SEProject1.db')
cur = conn.cursor()

class main:
    def __init__(self):
        # create main window
        self.main_window = tk.Tk()
        self.main_window.title('Coast Guard Task Manager')
        self.main_window.geometry('500x500')
        self.main_frame = tkinter.Frame(self.main_window)

        #Create buttons
        self.Add = tk.Button(self.main_frame, text='Add Task/Event', command=self.add)
        self.Remove = tk.Button(self.main_frame, text='Remove Task/Event', command=self.remove)
        self.Edit = tk.Button(self.main_frame, text='Edit Task/Event', command=self.edit)
        self.Calendar = tk.Button(self.main_frame, text='Calendar View', command=self.calendar)
        self.Todo = tk.Button(self.main_frame, text='To-do View', command=self.to_do)
        self.Priority = tk.Button(self.main_frame, text='Priority View', command=self.priority)
        self.Quit = tk.Button(self.main_frame, text='Quit', command=self.quit)

        #Create label
        self.label = tk.Label(self.main_frame, text='Hello! Please choose one of the options below')
        self.label.grid(row=1)

        #Pack
        self.main_frame.grid()
        self.Add.grid(row=2, column=1)
        self.Remove.grid(row=3, column=1)
        self.Edit.grid(row=4, column=1)
        self.Calendar.grid(row=5, column=1)
        self.Todo.grid(row=6, column=1)
        self.Priority.grid(row=7, column=1)
        self.Quit.grid(row=8, column=1)

        tkinter.mainloop()

    def quit(self):
        cur.close()
        conn.close()
        self.main_window.destroy()

    def add(self):
        #Code to add a task/event

    def remove(self):
        #Code to remove task/event

    def edit(self):
        #Code to edit task/event

    def calendar(self):
        #Code that calls the code from the calendar.py functions

    def to_do(self):
        #Code that calls the code from the to_do.py functions

    def priority(self):
        #Code that calls the code from the priority.py functions


if __name__ == '__main__':
    main()