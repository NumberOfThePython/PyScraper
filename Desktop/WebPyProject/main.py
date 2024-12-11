import tkinter as tk
from tkinter import messagebox
from dead_linker import check_dead_link

def on_check_link():
    url = url_entry.get()
    if url:
        result = check_dead_link(url)
        messagebox.showinfo("Status", result)
    else:
        messagebox.showwarning("Podaj URL.")

