from tkinter import *
root=Tk()
v= IntVar()
Radiobutton(root,text='GFG',variable=v,value=1).pack(anchor=W)
Radiobutton(root,text='MIT',variable=v,value=1).pack(anchor=W)
mainloop()