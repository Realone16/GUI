from ast import Lambda
from logging import root
from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("Image Gallery")
root.iconbitmap("camera.ico")

#create image widgets
img1=ImageTk.PhotoImage(Image.open("pics/milan.jpg"))
img2=ImageTk.PhotoImage(Image.open("pics/sunrise.jpg"))
img3=ImageTk.PhotoImage(Image.open("pics/rainbow.jpeg"))
img4=ImageTk.PhotoImage(Image.open("pics/greenland.jpg"))
img5=ImageTk.PhotoImage(Image.open("pics/freefall.jpg"))
img6=ImageTk.PhotoImage(Image.open("pics/valley-sea.jpeg"))

#create image list
img_list=[img1, img2, img3, img4, img5, img6]

#Command function for btn_forward Button
def forward(num):
    global my_label
    global btn_forward
    global btn_back
    my_label.grid_forget()
    my_label=Label(image=img_list[num-1])
    my_label.grid(row=0, column=0, columnspan=3, pady=10)
    
    #update btn_forward and btn_back Button widgets
    btn_forward=Button(root, text=">>", command=lambda: forward(num+1))
    btn_back=Button(root, text="<<", command=lambda: back(num-1))
    
    #position the updated btn_forward and btn_back Button widgets
    btn_forward.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)
    
    #Disable the btn_forward Button at the end of the images
    if num==6:
        btn_forward=Button(root, text=">>", state=DISABLED)
        btn_forward.grid(row=1, column=2)
    
    #Update the status bar
    status=Label(root,text="Image "+str(num)+" of "+str(len(img_list)), 
    bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E, pady=15)

#Command function for btn_back Button 
def back(num):
    global my_label
    global btn_forward
    global btn_back
    my_label.grid_forget()
    my_label=Label(image=img_list[num-1])
    my_label.grid(row=0, column=0, columnspan=3, pady=10)
    
    #update btn_forward and btn_back Button widgets
    btn_forward=Button(root, text=">>", command=lambda: forward(num+1))
    btn_back=Button(root, text="<<", command=lambda: back(num-1))
    
    #position the updated btn_forward and btn_back Button widgets
    btn_forward.grid(row=1, column=2)
    btn_back.grid(row=1, column=0)
    
    #Disable the btn_back Button at the end of the images
    if num==1:
        btn_back=Button(root, text="<<", state=DISABLED)
        btn_back.grid(row=1, column=0)
    
    #Update the status bar
    status=Label(root,text="Image "+str(num)+" of "+str(len(img_list)), 
    bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E, pady=15)

# create and position Label widget
my_label=Label(image=img1)
my_label.grid(row=0, column=0, columnspan=3, pady=10)

#Status bar using Label widget
status=Label(root, text="Image 1 0f "+str(len(img_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E, pady=15)

#create the Buttons widgets
btn_forward=Button(root, text=">>", command=lambda: forward(2))
btn_back=Button(root, text="<<", command=back)
btn_quit=Button(root, text="Exit Window", command=root.quit)

#position the Button widgets
btn_back.grid(row=1, column=0)
btn_quit.grid(row=1, column=1)
btn_forward.grid(row=1, column=2)
root.mainloop()