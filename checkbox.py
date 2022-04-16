from tkinter import *
root=Tk()
root.title("USING FILEDIALOG")
root.iconbitmap("icony/camera.ico")
root.geometry("400x400")

def show():
    lbl=Label(root, text=var.get()).pack()

var=StringVar()
c= Checkbutton(root, text="Are you well", 
variable=var, onvalue="ON", offvalue="OFF", command=show)
c.deselect()
c.pack()
lbl=Label(root, text=var.get()).pack()

root.mainloop()