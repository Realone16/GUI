from tkinter import *
from tkinter import messagebox

root=Tk()
root.title("MESSAGE-BOX")

def callup():
   #showinfo,showwarning,showerror,askquestion,askokcancel,askyesno
   resp=messagebox.askokcancel("What is happening", "Welcome Message!")
   if resp==1:
          Label(root, text="OK").pack()
   else:
          Label(root, text="CANCELLED").pack()

btn=Button(root, text="Click Message!!",command=callup)
btn.pack()
root.mainloop()