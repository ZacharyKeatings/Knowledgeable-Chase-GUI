import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Knowledgeable Chase")
root.geometry('300x200')

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

#Main Menu
login_button = ttk.Button(root, text="Add/Edit/Delete Trivia Database")
login_button.grid(column=1,row=0,pady=5)
log_button = ttk.Button(root, text="Get A Question")
log_button.grid(column=1,row=2,pady=5)
log_button = ttk.Button(root, text="Roll A Die")
log_button.grid(column=1,row=3,pady=5)
log_button = ttk.Button(root, text="Exit")
log_button.grid(column=1,row=4,pady=5)

root.mainloop()