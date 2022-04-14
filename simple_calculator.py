import math
from stat import FILE_ATTRIBUTE_NORMAL
from tkinter import *
root = Tk()
root.title("Simple calculator")
e=Entry(root, width=70, borderwidth=5)
e.grid(row=0, column=0, columnspan=4)

def button_click(number):
    current=e.get()
    e.delete(0, END)
    e.insert(0, str(current)+str(number))

def button_dot():
    f_number=e.get()
    e.delete(0, END)
    e.insert(0, str(f_number)+".")

def button_clear():
    e.delete(0, END)

def button_add():
    global f_num
    global mat
    f_num=e.get()
    mat="add"
    e.delete(0, END)
def button_subtract():
    global f_num
    global mat
    f_num=int(e.get())
    mat="-"
    e.delete(0, END)

def button_mul():
    global f_num
    global mat
    f_num=int(e.get())
    mat="X"
    e.delete(0, END)

def button_div():
    global f_num
    global mat
    f_num=int(e.get())
    mat="/"
    e.delete(0, END)

def button_modulus():
    global f_num
    global mat
    f_num=e.get()
    mat="%"
    e.delete(0, END)

def button_equal():
    second_num=e.get()
    e.delete(0, END)
    if mat=="add":
        e.insert(0, float(f_num) + float(second_num))
    if mat=="-":
        e.insert(0, f_num - int(second_num))
    if mat=="/":
        e.insert(0, f_num / int(second_num))
    if mat=="X":
        e.insert(0, f_num * int(second_num))
    if mat=="%":
        e.insert(0, int(f_num) % int(second_num))
#.....Create the Button widgets
one=Button(root, text="1", padx=40,pady=20, command=lambda: button_click(1))
two=Button(root, text="2", padx=40,pady=20, command=lambda: button_click(2))
three=Button(root, text="3", padx=40,pady=20, command=lambda: button_click(3))
four=Button(root, text="4", padx=40,pady=20, command=lambda: button_click(4))
five=Button(root, text="5", padx=40,pady=20, command=lambda: button_click(5))
six=Button(root, text="6", padx=40,pady=20, command=lambda: button_click(6))
seven=Button(root, text="7", padx=40,pady=20, command=lambda: button_click(7))
eight=Button(root, text="8", padx=40,pady=20, command=lambda: button_click(8))
nine=Button(root, text="9", padx=40,pady=20, command=lambda: button_click(9))
zero=Button(root, text="0", padx=40,pady=20, command=lambda: button_click(0))
dot=Button(root, text=".", padx=40,pady=20, command=button_dot)
clear=Button(root, text="Clear", padx=80,pady=20, command=button_clear)
add=Button(root, text="+", padx=40,pady=20, command=button_add)
minus=Button(root, text="-", padx=40,pady=20, command=button_subtract)
mul=Button(root, text="X", padx=40,pady=20, command=button_mul)
div=Button(root, text="/", padx=40,pady=20, command=button_div)
equal=Button(root, text="=", padx=80,pady=20, command=button_equal)
modulus=Button(root, text="%", padx=40,pady=20, command=button_modulus)
#....position the Button widgets
one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)
zero.grid(row=4, column=0)
modulus.grid(row=1, column=3)
add.grid(row=2, column=3)
minus.grid(row=3, column=3)
mul.grid(row=4, column=2)
div.grid(row=4, column=3)
clear.grid(row=5, column=0, columnspan=2)
equal.grid(row=5, column=2, columnspan=2)
dot.grid(row=4, column=1)

root.mainloop()