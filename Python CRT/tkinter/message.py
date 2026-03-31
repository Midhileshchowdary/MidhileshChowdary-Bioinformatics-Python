from tkinter import *
main=Tk()
ourMessage='This is Python class'
MessageVar= Message(main, text=ourMessage,width=1000)
MessageVar.config(bg='red')
MessageVar.pack()
main.mainloop()