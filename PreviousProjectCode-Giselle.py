import sqlite3
import tkinter
import tkinter as tk
import tkinter.messagebox


conn = sqlite3.connect('squadron_roster_3.db')
cur = conn.cursor()


class main:
    def __init__(self):
        # Create the squadron cadet roster window
        self.main_window = tkinter.Tk()
        self.main_window.title('Squadron Cadet Roster')

        # Frame in the squadron cadet roster window
        self.main_frame = tkinter.Frame(self.main_window)

        # Create buttons
        self.add_cadet = tkinter.Button(self.main_frame, text='Add Cadet',
                                        command=self.add_cadet)
        self.remove_cadet = tkinter.Button(self.main_frame, text='Remove Cadet',
                                           command=self.remove_cadet)
        self.edit_a_cadet = tkinter.Button(self.main_frame, text='Edit a Cadet',
                                           command=self.edit_cadet)
        self.print_roster = tkinter.Button(self.main_frame, text='Print Roster',
                                           command=self.print_roster)
        self.quit = tkinter.Button(self.main_frame, text='Quit',
                                   command=self.quit)

        # Create label
        self.label1 = tkinter.Label(self.main_window, text='Choose one of the following options')
        self.label1.grid(row=1)

        # grid/pack
        self.main_frame.grid()
        self.add_cadet.grid(row=2, column=1)
        self.remove_cadet.grid(row=3, column=1)
        self.edit_a_cadet.grid(row=4, column=1)
        self.print_roster.grid(row=5, column=1)
        self.quit.grid(row=6, column=2)

        tkinter.mainloop()

    # Create a function that ends the program
    def quit(self):
        cur.close()
        conn.close()
        self.main_window.destroy()

    def add_cadet(self):

        # Create add cadet window
        self.add_window = tkinter.Tk()
        self.add_window.title('Add Cadet')

        # Create add cadet frame
        # self.add_frame = tkinter.Frame(self.add_window)

        # Create label
        self.label_add = tkinter.Label(self.add_window, text='Enter the following information')
        self.label_add.grid(row=1, column=1)

        # Create entry widgets
        tk.Label(self.add_window, text='Cadet First Name').grid(row=2, column=2)
        tk.Label(self.add_window, text='Cadet Last Name').grid(row=3, column=2)
        tk.Label(self.add_window, text='Cadet Rank (Ex. C/Amn)').grid(row=4, column=2)
        tk.Label(self.add_window, text='Cadet CAPID').grid(row=5, column=2)

        self.first = tkinter.Entry(self.add_window)
        self.last = tkinter.Entry(self.add_window)
        self.rank = tkinter.Entry(self.add_window)
        self.ID = tkinter.Entry(self.add_window)

        # Create buttons
        self.back = tkinter.Button(self.add_window, text='Back', command=self.add_window.destroy)
        self.add = tkinter.Button(self.add_window, text='Add Cadet', command=self.add_finish)

        # grid everything
        self.first.grid(row=2, column=3)
        self.last.grid(row=3, column=3)
        self.rank.grid(row=4, column=3)
        self.ID.grid(row=5, column=3)
        self.back.grid(row=6, column=1)
        self.add.grid(row=6, column=3)



    def add_finish(self):

        global cur
        global conn
        # Get data info
        first = self.first.get()
        last = self.last.get()
        rank = self.rank.get()
        CAPID = self.ID.get()

        # Give the user a warning
        if tk.messagebox.askokcancel('Warning, adding the cadet to the database',
                                  'Check to make sure that all the data has been entered '
                                  'correctly; if all data is correct click OK.'):
        # Add to database
            sql = "INSERT INTO CADETS (CAPID, FIRST_NAME, LAST_NAME, RANK) VALUES (?,?,?,?)"
            values = CAPID, first, last, rank
            cur.execute(sql, values)
            conn.commit()
            self.add_window.destroy()

    def remove_cadet(self):
        # Create remove window
        self.remove_window = tkinter.Tk()
        self.remove_window.title('Remove Cadet')

        # Create window frame
        # self.remove_frame = tkinter.Frame(self.remove_window)

        # Create labels
        self.label_remove = tkinter.Label(self.remove_window, text='Enter the following information')
        self.label_remove.grid(row=1, column=2)

        # Create entry widgets
        tk.Label(self.remove_window, text='Cadet CAPID').grid(row=3, column=2)

        self.ID = tkinter.Entry(self.remove_window)
        self.ID.grid(row=3, column=3)

        # Create buttons
        self.back = tkinter.Button(self.remove_window, text='Back',
                                   command=self.remove_window.destroy).grid(row=5, column=1)
        self.remove = tkinter.Button(self.remove_window, text='Remove Cadet',
                                     command=self.remove_finish).grid(row=5, column=4)

    def remove_finish(self):
        global cur
        global conn

        # Get ingo
        ID = self.ID.get()

        # Send the user a warning
        if tk.messagebox.askokcancel('Warning, removing cadet from the database',
                                  'By clicking OK, this cadet will be permanently'
                                  ' removed from the roster. This action cannot be undone.'):
            # Add to database
            value = ID
            sql = "DELETE from CADETS where CAPID = ?"
            cur.execute(sql, (value,))
            conn.commit()
            self.remove_window.destroy()

    def edit_cadet(self):
        # Create edit window
        self.edit_window = tkinter.Tk()
        self.edit_window.title("Edit a Cadet's Information")

        # Create label
        self.label_edit = tkinter.Label(self.edit_window, text="Enter the cadet's CAPID")
        self.label_edit.grid(row=1, column=2)

        # Create entry widget
        tk.Label(self.edit_window, text='Cadet CAPID').grid(row=2, column=2)

        self.edit = tkinter.Entry(self.edit_window)
        self.edit.grid(row=2, column=3)

        # Create buttons
        self.back = tkinter.Button(self.edit_window, text='Back',
                                   command=self.edit_window.destroy).grid(row=3, column=1)
        self.edit_b = tkinter.Button(self.edit_window, text="Edit Cadet's info",
                                     command=self.edit_2).grid(row=3, column=3)

    def edit_2(self):
       # self.ID = float(self.edit.get())
        # Create edit window
        self.edit_2_window = tkinter.Tk()
        self.edit_2_window.title(f'Edit information for the cadet')
        self.edit_window.destroy()

        # Create frames
        self.frame1 = tkinter.Frame(self.edit_2_window)
        self.frame2 = tkinter.Frame(self.edit_2_window)

        # Create label
        self.edit_label = tkinter.Label(self.edit_2_window, text='Choose an option').grid(row=1, column=1)

        # Create option list
        tk.Radiobutton(self.edit_2_window, text='Cadet Last Name', value=1, command=self.option1).grid(row=2, column=1)
        tk.Radiobutton(self.edit_2_window, text='Cadet First Name', value=2, command=self.option2).grid(row=3, column=1)
        tk.Radiobutton(self.edit_2_window, text='Cadet Rank', value=3, command=self.option3).grid(row=4, column=1)
        tk.Radiobutton(self.edit_2_window, text='Cadet CAPID', value=4, command=self.option4).grid(row=5, column=1)

        # Create buttons
        self.back = tkinter.Button(self.edit_2_window, text='Cancel',
                                   command=self.edit_2_window.destroy).grid(row=6, column=1)

    def option1(self):
        # Create window
        self.option1_window = tkinter.Tk()
        self.option1_window.title('Edit Last Name')
        # Create labels an get info
        self.label = tkinter.Label(self.option1_window, text='Enter new cadet last name').grid(row=1, column=1)
        self.new = tkinter.Entry(self.option1_window)
        self.new.grid(row=1, column=2)

        self.label_edit = tkinter.Label(self.option1_window, text="Enter the cadet's CAPID")
        self.label_edit.grid(row=2, column=1)

        self.ID = tkinter.Entry(self.option1_window)
        self.ID.grid(row=2, column=2)
        # Create buttons
        self.back = tkinter.Button(self.option1_window, text='Back',
                                   command=self.option1_window.destroy).grid(row=3, column=1)
        self.Finish = tkinter.Button(self.option1_window, text='Finish',
                                     command=self.option1_finish).grid(row=3, column=2)

    def option1_finish(self):
        global cur
        global conn
        # Get info
        ID = self.ID.get()
        new = self.new.get()
        # Send the user a warning
        if tk.messagebox.askokcancel('Warning, editing this information',
                                     'By clicking OK, this information will be permanently'
                                     ' changed. This action cannot be undone.'):
            # Add to database
            value = new, ID
            sql = "UPDATE CADETS SET LAST_NAME = ? WHERE CAPID = ?"
            cur.execute(sql, value)
            conn.commit()
            self.option1_window.destroy()

    def option2(self):
        # Create window
        self.option2_window = tkinter.Tk()
        self.option2_window.title('Edit First Name')
        # Create labels and get info
        self.label = tkinter.Label(self.option2_window, text='Enter new cadet first name').grid(row=1, column=1)
        self.new = tkinter.Entry(self.option2_window)
        self.new.grid(row=1, column=2)

        self.label_edit = tkinter.Label(self.option2_window, text="Enter the cadet's CAPID")
        self.label_edit.grid(row=2, column=1)

        self.ID = tkinter.Entry(self.option2_window)
        self.ID.grid(row=2, column=2)

        # Create buttons
        self.back = tkinter.Button(self.option2_window, text='Back',
                                   command=self.option2_window.destroy).grid(row=3, column=1)
        self.Finish = tkinter.Button(self.option2_window, text='Finish',
                                     command=self.option2_finish).grid(row=3, column=2)

    def option2_finish(self):
        global cur
        global conn
        # Get info
        ID = self.ID.get()
        new = self.new.get()
        # Send user a warning
        if tk.messagebox.askokcancel('Warning, editing this information',
                                     'By clicking OK, this information will be permanently'
                                     ' changed. This action cannot be undone.'):
            # Add to database
            value = new, ID
            sql = "UPDATE CADETS SET FIRST_NAME = ? WHERE CAPID = ?"
            cur.execute(sql, value)
            conn.commit()
            self.option2_window.destroy()

    def option3(self):
        # Create window
        self.option3_window = tkinter.Tk()
        self.option3_window.title('Edit Rank')
        # Create labels and get info
        self.label = tkinter.Label(self.option3_window, text='Enter new cadet rank').grid(row=1, column=1)
        self.new = tkinter.Entry(self.option3_window)
        self.new.grid(row=1, column=2)

        self.label_edit = tkinter.Label(self.option3_window, text="Enter the cadet's CAPID")
        self.label_edit.grid(row=2, column=1)

        self.ID = tkinter.Entry(self.option3_window)
        self.ID.grid(row=2, column=2)
        # Create buttons
        self.back = tkinter.Button(self.option3_window, text='Back',
                                   command=self.option3_window.destroy).grid(row=3, column=1)
        self.Finish = tkinter.Button(self.option3_window, text='Finish',
                                     command=self.option3_finish).grid(row=3, column=2)

    def option3_finish(self):
        global cur
        global conn
        # Get info
        ID = self.ID.get()
        new = self.new.get()
        # Send user a warning
        if tk.messagebox.askokcancel('Warning, editing this information',
                                     'By clicking OK, this information will be permanently'
                                     ' changed. This action cannot be undone.'):
            # Add to database
            value = new, ID
            sql = "UPDATE CADETS SET RANK = ? WHERE CAPID = ?"
            cur.execute(sql, value)
            conn.commit()
            self.option3_window.destroy()

    def option4(self):
        # Create window
        self.option4_window = tkinter.Tk()
        self.option4_window.title('Edit Cadet CAPID')
        # Create label and get info
        self.label = tkinter.Label(self.option4_window, text='Enter new cadet CAPID').grid(row=1, column=1)
        self.new = tkinter.Entry(self.option4_window)
        self.new.grid(row=1, column=2)

        self.label_edit = tkinter.Label(self.option4_window, text="Enter the cadet's old CAPID")
        self.label_edit.grid(row=2, column=1)

        self.ID = tkinter.Entry(self.option4_window)
        self.ID.grid(row=2, column=2)

        # Create buttons
        self.back = tkinter.Button(self.option4_window, text='Back',
                                   command=self.option4_window.destroy).grid(row=3, column=1)
        self.Finish = tkinter.Button(self.option4_window, text='Finish',
                                     command=self.option4_finish).grid(row=3, column=2)

    def option4_finish(self):
        global cur
        global conn
        # Get info
        ID = self.ID.get()
        new = self.new.get()
        # Send user a warning
        if tk.messagebox.askokcancel('Warning, editing this information',
                                     'By clicking OK, this information will be permanently'
                                     ' changed. This action cannot be undone.'):
            # Add to database
            value = new, ID
            sql = "UPDATE CADETS SET CAPID = ? WHERE CAPID = ?"
            cur.execute(sql, value)
            conn.commit()
            self.option4_window.destroy()

    def print_roster(self):
        global cur
        global conn
        # Create roster window
        self.roster_window = tkinter.Tk()
        self.roster_window.title('Cadet Roster')

        # Create frames
        self.top_framer = tkinter.Frame(self.roster_window).grid()
        self.bottom_framer = tkinter.Frame(self.roster_window).grid()

        # Create label
        self.label = tkinter.Label(self.roster_window, text='Here is the cadet roster').grid()

        # Get info and write info
        cur.execute("SELECT * FROM CADETS")
        results = cur.fetchall()
        conn.commit()
        for row in results:
            tkinter.Label(self.roster_window, text=f'CAPID: {row[0]}').grid()
            tkinter.Label(self.roster_window, text=f'First Name: {row[1]}').grid()
            tkinter.Label(self.roster_window, text=f'Last Name: {row[2]}').grid()
            tkinter.Label(self.roster_window, text=f'Rank: {row[3]}').grid()
            tkinter.Label(self.roster_window).grid()

        # Create buttons
        self.done = tkinter.Button(self.roster_window, text='Done',
                                   command=self.roster_window.destroy).grid(row=2, column=3)

# Call the main class
if __name__ == '__main__':
    main()
