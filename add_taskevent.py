import sqlite3
import tkinter
import tkinter as tk
import tkinter.messagebox

conn = sqlite3.connect('Project2.db')
cur = conn.cursor()

class Add:


    def add(self):
        # Code to add a task/event
        '''taskevent = 'Test 1'
        details = 'Test in CRM'
        priority = 1
        date = 'April 1'
        sql = "INSERT INTO Main (TASKEVENT, DETAILS, PRIORITY, DATE) VALUES (?,?,?,?)"
        values = taskevent, details, priority, date
        cur.execute(sql, values)
        conn.commit()'''
        self.add_window = tk.Tk()
        self.add_window.title('Add Task/Event')
        self.frame1 = tkinter.Frame(self.add_window)
        self.frame2 = tkinter.Frame(self.add_window)

        self.add_label = tkinter.Label(self.frame1, text='Choose to add a task or event')

        # Options for event or task
        tk.Radiobutton(self.add_window, text='Add Task', value=1, command=Add.task(self)).grid(row=2, column=1)
        tk.Radiobutton(self.add_window, text='Add Event', value=2, command=Add.event).grid(row=3, column=1)

        self.back = tkinter.Button(self.add_window, text='Cancel', command=self.add_window.destroy).grid(row=4, column=1)

    def task(self):
        self.task_window = tkinter.Tk()
        self.task_window.title('Task')
        self.task_frame = tkinter.Frame(self.task_window)

        # Enter the new task
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

        # Back and finish buttons
        self.back = tkinter.Button(self.task_window, text='Back',
                                   command=self.task_window.destroy).grid(row=5, column=1)

        self.finish = tkinter.Button(self.task_window, text='Finish', command=Add.task_finish).grid(row=5,
                                                                                                     column=2)

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

        self.label3 = tkinter.Label(self.event_window, text='Enter date for event (YYYY/MM/DD)').grid(row=4,
                                                                                                      column=1)
        self.new_date = tkinter.Entry(self.event_window)
        self.new_date.grid(row=4, column=2)

        # Back and finish buttons
        self.back = tkinter.Button(self.event_window, text='Back',
                                   command=self.event_window.destroy).grid(row=5, column=1)

        self.finish = tkinter.Button(self.event_window, text='Finish', command=self.event_finish).grid(row=5,
                                                                                                       column=2)

    def event_finish(self):
        # insert into database
        value = 'Event', self.new_event.get(), self.new_event.get(), self.new_event.get(), self.new_event.get()
        sql = "INSERT INTO Main (TYPE, TASKEVENT, DETAILS, PRIORITY, DATE) VALUES (?,?,?,?,?)"
        cur.execute(sql, value)
        conn.commit()
        self.task_window.destroy()