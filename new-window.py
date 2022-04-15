from tkinter import *
from PIL import ImageTk, Image

root=Tk()
root.title("Working with tkinter")
root.iconbitmap('icony/camera.ico')
def open():
    global img
    top=Toplevel()
    top.title("Using Frame in Tkinter")
    top.iconbitmap('icony/camera.ico')
    img=ImageTk.PhotoImage(Image.open("icony/milan.jpg"))
    lbl=Label(top, image=img)
    lbl.pack()
    btn=Button(top, text="End Window", command=top.destroy)
    btn.pack()

btn2=Button(root, text="ENTER WINDOW", command=open)
btn2.pack()
mainloop()
