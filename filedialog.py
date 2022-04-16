from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
root=Tk()
root.title("USING FILEDIALOG")
root.iconbitmap("icony/camera.ico")
root.geometry("400x400")

def open():
    global img
    root.filename=filedialog.askopenfilename(
        initialdir="C:/Users/user/Desktop/user2-git-training-v1/GUI/pics",
        title="Select a file",
        filetypes=(("png files","*.png"),("all files","*.*"))
        )

    lbl=Label(root, text=root.filename)
    lbl.pack()
    img=ImageTk.PhotoImage(Image.open(root.filename))
    img_lbl=Label(image=img)
    img_lbl.pack()
    Button(root, text="Close window",command=root.quit).pack()

btn=Button(root, text="OPEN FILE", command=open)
btn.pack()
root.mainloop()