from tkinter import *
win=Tk()
win.geometry("300x300")
name=Label(win,text="Neme",fg="red")
password=Label(win,text="Password",fg="red")
email=Label(win,text="email ID",fg="red")
eN=Entry(win)
eP=Entry(win)
eE=Entry(win)
name.grid(row=0)
password.grid(row=1)
email.grid(row=2)
eN.grid(row=0,column=1)
eP.grid(row=1,column=1)
eE.grid(row=2,column=1)
win.mainloop()