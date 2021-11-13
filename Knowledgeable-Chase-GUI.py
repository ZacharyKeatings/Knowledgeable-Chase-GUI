import random
import tkinter as tk
from tkinter import ttk

#Create root window
root = tk.Tk()

#Define window title
root.title("Knowledgeable Chase")

#Define window dimensions
window_width = 300
window_height= 250
root.geometry("{}x{}".format(window_width, window_height))

# configure the grid
root.rowconfigure([0, 1, 2, 3, 4], weight=1)
root.columnconfigure([0, 1, 2], weight=1)

#Main title screen
def main_title():
    main_title = tk.Label(root, text="""Trivial Pursuit Assistant Edition\n
    ===================\n
    Please choose an option:""")
    main_title.place(width=window_width, height=window_height)
    main_title.grid(column=0,row=0,columnspan=3, sticky="NSEW")
    login_button = ttk.Button(root, text="Add/Edit/Delete Database", command=modify_database)
    login_button.grid(column=0,row=1,columnspan=3, sticky="NSEW")
    log_button = ttk.Button(root, text="Get A Question")
    log_button.grid(column=0,row=2,columnspan=3, sticky="NSEW")
    log_button = ttk.Button(root, text="Roll A Die")
    log_button.grid(column=0,row=3,columnspan=3, sticky="NSEW")
    log_button = ttk.Button(root, text="Exit", command=quit_program)
    log_button.grid(column=0,row=4,columnspan=3, sticky="NSEW")

#Page with options to alter database
def modify_database():
    title=tk.Label(root,text='Modify Database')
    title.place(width=window_width,height=window_height)
    title.grid(column=0,row=0,columnspan=3, sticky="NSEW")

    add=tk.Button(root,text='Add',command=add_trivia)
    add.grid(column=0,row=1,columnspan=3, sticky="NSEW")

    edit=tk.Button(root,text='Edit',command=edit_trivia)
    edit.grid(column=0,row=2,columnspan=3, sticky="NSEW")

    delete=tk.Button(root,text='Delete',command=delete_trivia)
    delete.grid(column=0,row=3,columnspan=3, sticky="NSEW")

    back=tk.Button(root,text='Back', command=main_title)
    back.grid(column=0,row=4,columnspan=3, sticky="NSEW")

#Add to database
def add_trivia():
    title=tk.Label(root,text='Add Trivia')
    title.place(width=window_width,height=window_height)
    title.grid(column=0,row=0,columnspan=3, sticky="NSEW")

#Edit database
def edit_trivia():
    title=tk.Label(root,text='Edit Trivia')
    title.place(width=window_width,height=window_height)
    title.grid(column=0,row=0,columnspan=3, sticky="NSEW")

#Delete from database
def delete_trivia():
    title=tk.Label(root,text='Delete Trivia')
    title.place(width=window_width,height=window_height)
    title.grid(column=0,row=0,columnspan=3, sticky="NSEW")

#Get question from database (Question, then answer)
def get_question():
    pass

#Closes program
def quit_program():
    root.destroy()

main_title()
root.mainloop()