from tkinter import *
root=Tk()
root.title("USING FILEDIALOG")
root.iconbitmap("icony/camera.ico")
root.geometry("400x400")
    
def size():
    root.geometry(str(y.get())+"x"+str(x.get()))
    Label(root, text="Horizontal: "+ str(x.get())).pack()
    Label(root, text="Vertical: "+ str(y.get())).pack()
    
y=Scale(root, from_=0, to=400)
y.pack()
x=Scale(root, from_=0, to=400, orient=HORIZONTAL)
x.pack()
btn=Button(root, text="Show Slider's value", command=size).pack()
root.mainloop()