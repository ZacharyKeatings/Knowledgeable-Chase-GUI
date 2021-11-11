import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Knowledgeable Chase")
root.geometry('400x300')

# configure the grid
root.rowconfigure([0, 1, 2, 3, 4], minsize=50, weight=1)
root.columnconfigure([0, 1, 2], minsize=50, weight=1)

#Main Menu
main_title = tk.Label(master=root, text="""Trivial Pursuit Assistant Edition\n
===================\n
Please choose an option:""")
main_title.grid(column=1,row=0)
login_button = ttk.Button(root, text="Add/Edit/Delete Database")
login_button.grid(column=1,row=1)
log_button = ttk.Button(root, text="Get A Question")
log_button.grid(column=1,row=2)
log_button = ttk.Button(root, text="Roll A Die")
log_button.grid(column=1,row=3)
log_button = ttk.Button(root, text="Exit")
log_button.grid(column=1,row=4)

root.mainloop()