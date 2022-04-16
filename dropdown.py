from tkinter import *
root=Tk()
root.title("USING FILEDIALOG")
root.iconbitmap("icony/camera.ico")
root.geometry("400x400")
options=[
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"

]

clicked=StringVar()
clicked.set(options[0])

def show(val):
    drop_lbl=Label(root, text=clicked.get())
    drop_lbl.pack()

drop=OptionMenu(root, clicked, *options, command=show)
drop.pack(pady=15)

drop_lbl=Label(root, text=clicked.get())
drop_lbl.pack(pady=15)
root.mainloop()