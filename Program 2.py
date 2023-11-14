from tkinter import *
from tkinter import simpledialog
from tkinter import Tk, ttk
import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import tkinter.font
from tkinter import font
from tkinter.simpledialog import Dialog

def popup():
    name = simpledialog.askstring ("Name", "What is your name?")
    while all((name.isalpha() or name.isspace()) for name in name) == False:
        messagebox.showerror('Invalid','Only letters and spaces are allowed!'),
        name = simpledialog.askstring ("Name", "What is your name?")
        while len(name) == 0:
            messagebox.showwarning("Oh oh", "you have to enter your name here")
            name = simpledialog.askstring ("Name", "What is your name?")
    while len(name) == 0:
        messagebox.showwarning("Oh oh", "you have to enter your name here")
        name = simpledialog.askstring ("Name", "What is your name?")
        while all((name.isalpha() or name.isspace()) for name in name) == False:
            messagebox.showerror('Invalid','Only letters and spaces are allowed!'),
            name = simpledialog.askstring ("Name", "What is your name?")
    print (name)
    
    age = simpledialog.askstring ("Age", "What is your age?")
    while len(age) == 0:
        messagebox.showwarning("Oh oh", "you have to enter your age here")
        age = simpledialog.askstring ("Age", "What is your age?")
        while all(age.isnumeric() for age in age) == False:
            messagebox.showerror('Invalid','Only numbers are allowed!'),
            age = simpledialog.askstring ("Age", "What is your age")
    while all(age.isnumeric() for age in age) == False:
        messagebox.showerror('Invalid','Only numbers are allowed!'),
        age = simpledialog.askstring ("Age", "What is your age")
        while len(age) == 0:
            messagebox.showwarning("Oh oh", "you have to enter your age here")
            age = simpledialog.askstring ("Age", "What is your age?")
    print (age)

    address = simpledialog.askstring ("Address", "What is your address?")
    while all((address.isalpha() or address.isspace()) for address in address) == False:
        messagebox.showerror('Invalid','Only letters are allowed!'),
        address = simpledialog.askstring ("Address", "What is your address?")
        while len(address) == 0:
            messagebox.showwarning("Oh oh", "you have to enter your address here")
            address = simpledialog.askstring ("Address", "What is your address")
    while len(address) == 0:
        messagebox.showwarning("Oh oh", "you have to enter your address here")
        address = simpledialog.askstring ("Address", "What is your address")
        while all((address.isalpha() or address.isspace()) for address in address) == False:
            messagebox.showerror('Invalid','Only letters are allowed!'),
            address = simpledialog.askstring ("Address", "What is your address?")
    print (address)
  
    label1.configure(text=str ((("My name is " + name))))
    label2.configure(text=str (("I am " + (age) + " years old")))
    label3.configure(text=str (("I live in " + address)))
    messagebox.showinfo("Success", "Data is Uploaded")
    
root = Tk() 
root.title ("Startup")
root.config(bg = "white")
font.families()

font1 = ("Terminal", 18, "bold")
label1 = Label(root, width = "36", height = "1",bg="white", fg="#2874A6")
label2 = Label(root, width = "36", height = "1",bg="white", fg="#2874A6")
label3 = Label(root, width = "36", height = "1",bg="white", fg="#2874A6")
label1.configure(font = font1)
label2.configure(font = font1)
label3.configure(font = font1)

button = Button(root, width = "15", height = "2", text = "Start", command = popup, bg="green", fg="white")
button.pack()
button1 = Button(root, width = "15", height = "2", text = "Stop", command = exit, bg="red", fg="white")
button.pack()

button.grid(row = 0, column = 4)
button1.grid(row = 1, column = 4)
label1.grid(row = 3, column = 5)
label2.grid(row = 4, column = 5)
label3.grid(row = 5, column = 5)

root.geometry("900x300")
root.resizable(False, False)

root.mainloop()

#name = input("What is your name? ")
#age = input("What is your age: ")
#address = input("What is your address: ")
#print()
#print("Name: " + name)
#print("Age: " + age)
#print("Address: " + address)
#text = input("Enter text: ")

