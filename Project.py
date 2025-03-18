import tkinter as tk
from tkinter import messagebox

# https://www.youtube.com/watch?v=Mtc402fS0Jw
def register():
    username = username_entry.get()

# CREATE MAIN gui window
root = tk.Tk()
root.geometry("300x300")
root.title("Registration form")

# set gui background color 
root.configure(background= "white")

# create and config and form frame
form_frame = tk.Frame(root, padx=20, pady=20)
form_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

#create configure registration button
register_button = tk.Button(form_frame, text = "Register", command=register)

#run tkinter main loop
root.mainloop()
