from datetime import date
from distutils.dep_util import newer
from logging import RootLogger

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
        self.Add = tk.Button(self.main_frame, text='Add Task/Event', command=self.add, height = 2, width = 15)
        self.Remove = tk.Button(self.main_frame, text='Remove Task/Event', command=self.remove, height = 2, width = 15)
        self.Edit = tk.Button(self.main_frame, text='Edit Task/Event', command=self.edit, height = 2, width = 15)
        self.Calendar = tk.Button(self.main_frame, text='Calendar View', command=self.calendar, height = 2, width = 15)
        self.Todo = tk.Button(self.main_frame, text='To-do View', command=self.to_do, height = 2, width = 15)
        self.Priority = tk.Button(self.main_frame, text='Priority View', command=self.priority, height = 2, width = 15)
        self.Quit = tk.Button(self.main_frame, text='Quit', command=self.quit, height = 2, width = 15)

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
        tk.Radiobutton(self.add_window, text='Add Task',value=1, command=self.task_clicked).grid(row=2, column=1)
        tk.Radiobutton(self.add_window, text='Add Event', value =2,  command=self.event_clicked).grid(row=3, column=1)

        self.back = tkinter.Button(self.add_window, text = 'Cancel', command=self.add_window.destroy).grid(row=4, column=1)

    def task_clicked(self):
        self.add_window.destroy()
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

        self.finish = tkinter.Button(self.task_window, text='Finish', command=self.task_finish_clicked). grid(row=5, column=2)

    def task_finish_clicked(self):

        # insert into database
        value = 'Task', self.new_task.get(), self.new_details.get(), self.new_priority.get(), self.new_date.get()
        sql = "INSERT INTO Main (TYPE, TASKEVENT, DETAILS, PRIORITY, DATE) VALUES (?,?,?,?,?)"
        cur.execute(sql, value)
        conn.commit()
        self.task_window.destroy()

    def event_clicked(self):
        self.add_window.destroy()
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

        self.finish = tkinter.Button(self.event_window, text='Finish', command=self.event_finish_clicked).grid(row=5, column=2)

    def event_finish_clicked(self):
        # insert into database
        self.event_window.destroy()
        value = 'Event', self.new_event.get(), self.new_details.get(), self.new_priority.get(), self.new_date.get()
        sql = "INSERT INTO Main (TYPE, TASKEVENT, DETAILS, PRIORITY, DATE) VALUES (?,?,?,?,?)"
        cur.execute(sql, value)
        conn.commit()
        self.task_window.destroy()

    def remove(self):
        #Code to remove task/event
        self.remove_window = tk.Tk()
        self.remove_window.title('Remove an event/task')

        self.label_remove = tk.Label(self.remove_window, text='Enter the following information to delete your event/task').grid(row=1, column=1)

        #Labels for required information
        tk.Label(self.remove_window, text='Enter event/task name').grid(row=2, column=1)
        tk.Label(self.remove_window, text='Enter date for event (YYYY/MM/DD)').grid(row=3, column=1)

        #Getting required inputs
        self.name = tk.Entry(self.remove_window)
        self.name.grid(row=2, column=2)

        self.date = tk.Entry(self.remove_window)
        self.date.grid(row=3, column=2)

        # Create buttons
        self.back = tkinter.Button(self.remove_window, text='Back',
                                   command=self.remove_window.destroy).grid(row=4, column=1)
        self.remove = tkinter.Button(self.remove_window, text='Remove Event/Task',
                                     command=self.remove_clicked).grid(row=4, column=4)

    def remove_clicked(self):
        #Removes the event/task in the database
        name = self.name.get()
        date = self.date.get()

        #Remove from database
        value = name, date
        sql = "DELETE from Main where TASKEVENT = ? AND DATE = ?"
        cur.execute(sql, value)
        conn.commit()
        self.remove_window.destroy()

    def edit(self):
        #Code to edit task/event
        self.edit_window = tk.Tk()
        self.edit_window.title('Edit an event/task')

        #Lables
        self.edit_window.label = tkinter.Label(self.edit_window, text='Enter type (event or task)').grid(row=2, column=1)
        self.edit_window.label = tkinter.Label(self.edit_window, text='Enter the event name').grid(row=3, column=1)
        self.edit_window.label = tkinter.Label(self.edit_window, text='Enter date (YYYY/MM/DD)').grid(row=4, column=1)

        #Entry windows
        self.type = tk.Entry(self.edit_window).grid(row=2, column=2)
        self.event_task = tk.Entry(self.edit_window).grid(row=3, column=2)
        self.date = tk.Entry(self.edit_window).grid(row=4, column=2)

        #Buttons
        self.back = tkinter.Button(self.edit_window, text='Back',
                                   command=self.edit_window.destroy).grid(row=5, column=1)
        self.edit_ = tkinter.Button(self.edit_window, text='Edit Event/Task',
                                     command=self.edit_clicked).grid(row=5, column=4)

    def edit_clicked(self):
        # Create window
        self.edit_clicked_window = tk.Tk()
        self.edit_clicked_window.title('Select what you want to change about your event/task')

        # Options for editing task/event
        tk.Radiobutton(self.edit_clicked_window, text='Type (Event/task)', value=1, command=self.edit_type).grid(row=2, column=1)
        tk.Radiobutton(self.edit_clicked_window, text='Name', value=2, command=self.edit_name).grid(row=3, column=1)
        tk.Radiobutton(self.edit_clicked_window, text='Details', value=3, command=self.edit_details).grid(row=4, column=1)
        tk.Radiobutton(self.edit_clicked_window, text='Priority', value=4, command=self.edit_priority).grid(row=5, column=1)
        tk.Radiobutton(self.edit_clicked_window, text='Date', value=5, command=self.edit_date).grid(row=6, column=1)

        self.edit_window.destroy()

        #get info from previous screen
        type = self.type.get()
        event_task = self.event_task.get()
        date = self.date.get()

        # Edit from database
        value = event_task, date, type
        sql = "SELECT * from Main where TASKEVENT = ? AND DATE = ? AND TYPE = ?"
        cur.execute(sql, value)
        result = cur.fetchall()
        conn.commit()
        for row in result:
            Type = row[0]
            Task_event = row[1]
            Details = row[2]
            Priority = row[3]
            Date = row[4]
    def edit_type(self):
        self.Type.get()


    def edit_name(self):
        pass

    def edit_details(self):
        pass

    def edit_priority(self):
        pass

    def edit_date(self):
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

        '''right now this code is just to print what's in the database for testing
        pruposes. This is not the actual code for this function'''
        self.roster_window = tkinter.Tk()
        self.roster_window.title('Database')

        # Create frames
        self.top_framer = tkinter.Frame(self.roster_window).grid()
        self.bottom_framer = tkinter.Frame(self.roster_window).grid()


        # Get info and write info
        cur.execute("SELECT * FROM Main")
        results = cur.fetchall()
        conn.commit()
        for row in results:
            tkinter.Label(self.roster_window, text=f'Type: {row[0]}').grid()
            tkinter.Label(self.roster_window, text=f'Task/Event Name: {row[1]}').grid()
            tkinter.Label(self.roster_window, text=f'Details: {row[2]}').grid()
            tkinter.Label(self.roster_window, text=f'Priority: {row[3]}').grid()
            tkinter.Label(self.roster_window, text=f'Date: {row[4]}').grid()
            tkinter.Label(self.roster_window).grid()

        # Create buttons
        self.done = tkinter.Button(self.roster_window, text='Done',
                                   command=self.roster_window.destroy).grid(row=2, column=3)


if __name__ == '__main__':
    main()