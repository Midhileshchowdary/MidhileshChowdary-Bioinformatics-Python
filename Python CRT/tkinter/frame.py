from tkinter import *
root = Tk()
frame=Frame(root)
frame.pack()
bottomframe=Frame(root)
bottomframe.pack(side=BOTTOM)
redbutton= Button(frame, text='1',fg='red')
redbutton.pack()
mainloop()
