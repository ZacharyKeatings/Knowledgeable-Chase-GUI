import random
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Knowledgeable Chase")
root.geometry("400x300")

# configure the grid
root.rowconfigure([0, 1, 2, 3, 4], minsize=10, weight=1)
root.columnconfigure([0, 1, 2], minsize=10, weight=1)

def die_roll():

    def roll_outcome():
        dice_number = random.choice([1,2,3,4,5,6])
        print(dice_number)

    #This shows in the GUI:
    roll = tk.Tk()
    roll.title("Die Roll")
    roll.geometry("400x300")
    roll.rowconfigure([0,1], minsize=10, weight=1)
    roll.columnconfigure([0,1,2], minsize=10, weight=1)

    roll_result = tk.Label(roll, text="Roll result:")
    print(roll_outcome())
    roll_result.grid(column=1, row=0, sticky="S")
    roll_again = ttk.Button(roll, text="Roll Again", command=roll_outcome)
    roll_again.grid(column=1, row=1, sticky="W")
    main_menu = ttk.Button(roll, text="Main Menu", command=lambda:root.mainloop())
    main_menu.grid(column=1, row=1, sticky="E")

#Main Menu
main_title = tk.Label(root, text="""Trivial Pursuit Assistant Edition\n
===================\n
Please choose an option:""")
main_title.grid(column=1,row=0)
login_button = ttk.Button(root, text="Add/Edit/Delete Database", width=20)
login_button.grid(column=1,row=1)
log_button = ttk.Button(root, text="Get A Question", width=20)
log_button.grid(column=1,row=2)
log_button = ttk.Button(root, text="Roll A Die", width=20, command=die_roll)
log_button.grid(column=1,row=3)
log_button = ttk.Button(root, text="Exit", width=20)
log_button.grid(column=1,row=4)





root.mainloop()