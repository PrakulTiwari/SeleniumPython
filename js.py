import tkinter as tk
import time
from tkinter import messagebox

root = tk.Tk()
root.geometry('500x500')
root.title('Do nothing Eat 5 Star')

name = tk.Entry(root)
name.pack(pady=10)


def click():
    nm = name.get()
    nm.lower()
    if 'prakul' in nm:
        messagebox.showerror('Err', 'PRAKUL!!')
    else:
        messagebox.showinfo('Ok', 'OK')
        quit()


btn = tk.Button(root, text="Click Here!", command=click)
btn.pack(pady=10)

root.mainloop()
