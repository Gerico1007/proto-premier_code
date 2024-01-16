import tkinter as tk

def say_hello():
    name = name_entry.get()
    greeting_label.config(text="Hello " + name)

root = tk.Tk()
root.title("Hello World CLI")

name_entry = tk.Entry(root)
name_entry.pack()

hello_button = tk.Button(root, text="Say Hello", command=say_hello)
hello_button.pack()

greeting_label = tk.Label(root, text="")
greeting_label.pack()

root.mainloop()