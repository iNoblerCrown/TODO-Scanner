from todoscanner import *
import tkinter as tk
import os
import subprocess
a, b, c = None, None, None

def submit():
    global a, b, c
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()
    fileEndings = formatFileEnding(a)
    file = open("found.txt", "w")
    file.write(str(main(fileEndings, b, c)))
    file.close()


def formatFileEnding(a):
    x = a.split(", ")
    return x

def getDefault():
    global da, db, dc
    file = open("defaultsave.txt", "r")
    x = file.read().split("\n")
    da, db, dc = x[0], x[1], x[2]

def saveDefault():
    global a, b, c
    da, db, dc = a, b, c
    file = open("defaultsave.txt", "w")
    file.write(f"{da}\n{db}\n{dc}")
    file.close()

# Create the Tkinter window
root = tk.Tk()
try:
    getDefault()
except:
    ""

root.title("TODO-Finder by Kadir | Copyright Kadir Aras Yanar FROG")
root.iconbitmap("logo.ico")

# Create the input fields and labels
label_a = tk.Label(root, text="File ending: (format: '.java')")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()
try:
    entry_a.insert(0, da)
except:
    ""

label_b = tk.Label(root, text="Directory: (use '/' instead of *backslash*)")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()
try:
    entry_b.insert(0, db)
except:
    ""

label_c = tk.Label(root, text="TODO Keyword:")
label_c.pack()
entry_c = tk.Entry(root)
entry_c.pack()
try:
    entry_c.insert(0, dc)
except:
    ""

# Create the submit button
submit_button = tk.Button(root, text="Search for TODO", command=submit)
submit_button.pack()

default_button = tk.Button(root, text="Set current as default", command=lambda: saveDefault())
default_button.pack()

file = open("found.txt", "r")
variable_label = tk.Label(root, text=f"Found TODOs:\n{file.read()}")
variable_label.pack()

# Start the Tkinter event loop
root.mainloop()