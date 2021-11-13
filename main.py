import random
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Knowledgeable Chase")
height = 300
width = 250
root.geometry("{}x{}".format(width, height))

frame=tk.Frame(root)
frame.place(height=300, width=400)

# configure the grid
root.rowconfigure([0, 1, 2, 3, 4], weight=1)
root.columnconfigure([0, 1, 2], weight=1)



def view_database():

    def add_trivia():
        label=tk.Label(frame,text='this is the page2')
        label.place(relx=0.3,rely=0.4)

    def edit_trivia():
        label=tk.Label(frame,text='this is the page3')
        label.place(relx=0.3,rely=0.4)

    def delete_trivia():
        label=tk.Label(frame,text='this is the page3')
        label.place(relx=0.3,rely=0.4)

    add=tk.Button(root,text='Add',command=add_trivia)
    add.grid(column=0,row=0)

    edit=tk.Button(root,text='Edit',command=edit_trivia)
    edit.grid(row=0,column=1)

    delete=tk.Button(root,text='Delete',command=delete_trivia)
    delete.grid(row=0,column=2)

def die_roll():

    def roll_outcome():
        dice_number = random.choice([1,2,3,4,5,6])
        return dice_number

    #This shows in the GUI:
    roll = tk.Tk()
    roll.title("Die Roll")
    roll.geometry("{}x{}".format(width, height))
    roll.rowconfigure([0,1], minsize=10, weight=1)
    roll.columnconfigure([0,1,2], minsize=10, weight=1)

    roll_result = tk.Label(roll, text="Roll result:")
    roll_result.grid(column=1, row=0, sticky="S")
    roll_again = ttk.Button(roll, text="Roll Again", command=roll_outcome)
    roll_again.grid(column=1, row=1, sticky="W")
    main_menu = ttk.Button(roll, text="Main Menu", command=lambda:root.mainloop())
    main_menu.grid(column=1, row=1, sticky="E")

def close_app():
    label=tk.Label(frame,text='this is the page3')
    label.place(relx=0.3,rely=0.4)



main_title = tk.Label(root, text="""Trivial Pursuit Assistant Edition\n
===================\n
Please choose an option:""")
main_title.place(width=width, height=height)
main_title.grid(column=0,row=0,columnspan=3, sticky="NSEW")
login_button = ttk.Button(root, text="Add/Edit/Delete Database", command=view_database)
login_button.grid(column=0,row=1,columnspan=3, sticky="NSEW")
log_button = ttk.Button(root, text="Get A Question")
log_button.grid(column=0,row=2,columnspan=3, sticky="NSEW")
log_button = ttk.Button(root, text="Roll A Die", command=die_roll)
log_button.grid(column=0,row=3,columnspan=3, sticky="NSEW")
log_button = ttk.Button(root, text="Exit")
log_button.grid(column=0,row=4,columnspan=3, sticky="NSEW")

root.mainloop()