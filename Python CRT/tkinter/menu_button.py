from tkinter import *
top=Tk()
mb=Menubutton(top, text='course',relief=RAISED)
mb.grid()
mb.menu=Menu(mb, tearoff=0)
mb["menu"]=mb.menu
mayoVar= IntVar()
ketchVar= IntVar()
mb.menu.add_checkbutton(label="Btech",variable=mayoVar)
mb.menu.add_checkbutton(label="Bsc",variable=mayoVar)
mb.pack()
top.mainloop()