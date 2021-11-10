import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Knowledgeable Chase")
root.geometry('300x200')

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)

#test Button
login_button = ttk.Button(root, text="Login")
login_button.grid(column=1,row=0,pady=5)
log_button = ttk.Button(root, text="Login")
log_button.grid(column=1,row=1,pady=5)


root.mainloop()