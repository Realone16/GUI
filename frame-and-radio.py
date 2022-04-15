from cgitb import text
from tkinter import *
'''
root=Tk()
root.title("Using frame in Tkinter")
root.iconbitmap("icony/camera.ico")
frame=LabelFrame(root,text="New Frame", padx=10, pady=10)
frame.pack(padx=20,pady=20)
Button(frame, text="Click me!!").grid(row=0, column=0)
Button(frame, text="Welcome!!").grid(row=1, column=1)
root.mainloop()
'''
root=Tk()
root.title("Using Radio in Tkinter")
root.iconbitmap("icony/camera.ico")
#Create a list
MODES=[
    ("cheese","cheese"),
    ("pepperoni","pepperoni"),
    ("carrot","carrot"),
    ("onions","onions"),
    ("garlic","garlic"),
]
#state the variable
pizza=StringVar()
pizza.set("pepperoni")

#Command function
def call(val):
    lbl=Label(root, text=val)
    lbl.pack()
    
#declare the Radiobutton widgets using for loops
for but,ton in MODES: 
    Radiobutton(root, text=but, variable=pizza, value=ton).pack(anchor=W)

#show result
#lbl=Label(root, text=pizza.get())
#lbl.pack()

#create a button
btn=Button(root, text="INSERT",command=lambda: call(pizza.get()))
btn.pack(pady=10)
root.mainloop()