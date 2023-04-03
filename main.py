from tkinter import *
import os

docu_dir = os.path.join(os.path.expanduser("~"), "Downloads")

window = Tk()
window.geometry("800x600")
window.title("Test")
window.resizable(False, False)

global_font = ("Roboto", 30, "bold")
header = Label(window, text="To-Do", fg="dark orange", font=global_font)
header.pack()

def add_task():
    task = input_task.get()
    print(task)
    task_list = Listbox(window)
    task_list.insert(task)
    task_list.pack()

add_button = Button(window, text="Add", bg="black", fg="red", command=add_task)
add_button.pack(pady=10)

input_task = Entry(window)
input_task.pack(pady=10)

window.mainloop()