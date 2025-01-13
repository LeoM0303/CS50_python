import tkinter as tk
from tkinter import messagebox

def check_name():
    name = entry.get()
    messages = {
        "Harry": "You are a wizard!",
        "Hermione": "You are a wizard!",
        "Ron": "You are a wizard!",
        "Dobby": "You are a free elf!",
        "Voldemort": "You are a dark wizard!",
        "Draco": "You are a death eater",
        "Snape": "You are a half-blood prince",
        # Add more names and messages as needed
    }
    message = messages.get(name, "Who are you?")
    messagebox.showinfo("Result", message)
 
root = tk.Tk()
root.title("Potter Character Checker")
root.geometry("300x200")

label = tk.Label(root, text="What is your name?")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Check", command=check_name)
button.pack(pady=10)

root.mainloop()
