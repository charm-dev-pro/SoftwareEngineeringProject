from datetime import date
from distutils.dep_util import newer

import calendar
import priority
#import to_do
import sqlite3
import tkinter
import tkinter as tk
import tkinter.messagebox

'''from calendar import Calendar
from to_do import To_do'''

conn = sqlite3.connect('Project2.db')
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

        #Pack/view of buttons on window
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
        '''taskevent = 'Test 1'
        details = 'Test in CRM'
        priority = 1
        date = 'April 1'
        sql = "INSERT INTO Main (TASKEVENT, DETAILS, PRIORITY, DATE) VALUES (?,?,?,?)"
        values = taskevent, details, priority, date
        cur.execute(sql, values)
        conn.commit()'''
        self.add_window = tkinter.Tk()
        self.add_window.title('Add Task/Event')
        self.frame1 = tkinter.Frame(self.add_window)
        self.frame2 = tkinter.Frame(self.add_window)

        self.add_label = tkinter.Label(self.frame1, text='Choose to add a task or event')


        #Options for event or task
        tk.Radiobutton(self.add_window, text='Add Task',value=1, command=self.task).grid(row=2, column=1)
        tk.Radiobutton(self.add_window, text='Add Event', value =2,  command=self.event).grid(row=3, column=1)

        self.back = tkinter.Button(self.add_window, text = 'Cancel', command=self.add_window.destroy).grid(row=4, column=1)

    def task(self):
        self.task_window = tkinter.Tk()
        self.task_window.title('Task')
        self.task_frame = tkinter.Frame(self.task_window)

        #Enter the new task
        self.label = tkinter.Label(self.task_window, text='Enter task name').grid(row=1, column=1)
        self.new_task = tkinter.Entry(self.task_window)
        self.new_task.grid(row=1, column=2)

        self.label1 = tkinter.Label(self.task_window, text='Enter task details').grid(row=2, column=1)
        self.new_details = tkinter.Entry(self.task_window)
        self.new_details.grid(row=2, column=2)

        self.label2 = tkinter.Label(self.task_window, text='Enter priority (eg. 1)').grid(row=3, column=1)
        self.new_priority = tkinter.Entry(self.task_window)
        self.new_priority.grid(row=3, column=2)

        self.label3 = tkinter.Label(self.task_window, text='Enter date for task (YYYY/MM/DD)').grid(row=4, column=1)
        self.new_date = tkinter.Entry(self.task_window)
        self.new_date.grid(row=4, column=2)

        #Back and finish buttons
        self.back = tkinter.Button(self.task_window, text='Back',
                                   command=self.task_window.destroy).grid(row=5, column=1)

        self.finish = tkinter.Button(self.task_window, text='Finish', command=self.task_finish). grid(row=5, column=2)

    def task_finish(self):
        # insert into database
        value = 'Task', self.new_task.get(), self.new_details.get(), self.new_priority.get(), self.new_date.get()
        sql = "INSERT INTO Main (TYPE, TASKEVENT, DETAILS, PRIORITY, DATE) VALUES (?,?,?,?,?)"
        cur.execute(sql, value)
        conn.commit()
        self.task_window.destroy()

    def event(self):
        self.event_window = tkinter.Tk()
        self.event_window.title('Event')
        self.event_frame = tkinter.Frame(self.event_window)

        # Enter the new event
        self.label = tkinter.Label(self.event_window, text='Enter event name').grid(row=1, column=1)
        self.new_event = tkinter.Entry(self.event_window)
        self.new_event.grid(row=1, column=2)

        self.label1 = tkinter.Label(self.event_window, text='Enter event details').grid(row=2, column=1)
        self.new_details = tkinter.Entry(self.event_window)
        self.new_details.grid(row=2, column=2)

        self.label2 = tkinter.Label(self.event_window, text='Enter priority (eg. 1)').grid(row=3, column=1)
        self.new_priority = tkinter.Entry(self.event_window)
        self.new_priority.grid(row=3, column=2)

        self.label3 = tkinter.Label(self.event_window, text='Enter date for event (YYYY/MM/DD)').grid(row=4, column=1)
        self.new_date = tkinter.Entry(self.event_window)
        self.new_date.grid(row=4, column=2)

        # Back and finish buttons
        self.back = tkinter.Button(self.event_window, text='Back',
                                   command=self.event_window.destroy).grid(row=5, column=1)

        self.finish = tkinter.Button(self.event_window, text='Finish', command=self.event_finish).grid(row=5, column=2)

    def event_finish(self):
        # insert into database
        value = 'Event', self.new_event.get(), self.new_event.get(), self.new_event.get(), self.new_event.get()
        sql = "INSERT INTO Main (TYPE, TASKEVENT, DETAILS, PRIORITY, DATE) VALUES (?,?,?,?,?)"
        cur.execute(sql, value)
        conn.commit()
        self.task_window.destroy()

    def remove(self):
        #Code to remove task/event
        pass

    def edit(self):
        #Code to edit task/event
        pass

    def calendar(self):
        #Code that calls the code from the calendar.py functions
        pass
        '''Example below of how to call a method from another .py file
        Calendar.test(self)'''
    def to_do(self):
        #Code that calls the code from the to_do.py functions
        pass

    def priority(self):
        #Code that calls the code from the priority.py functions
        pass

if __name__ == '__main__':
    main()