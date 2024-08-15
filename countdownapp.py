from tkinter import *
def get_time():
    t=int(time_var.get())
    if t>0:
        t=t-1
        time_var.set(t)
        win.after(1000,get_time)
win=Tk()
win.geometry("300x300")
global enter1
win.config(bg="gray")
win.title("COUNTDOWN APP")
time_var=StringVar()
enter1=Entry(win,textvariable=time_var,justify="center",font=("Time New Roman",20,"bold"))
enter1.place(x=45,y=50,height=50,width=200)
button1=Button(win,text="countdown",font=("Time New Roman",12,"bold"),command=get_time)
button1.place(x=85,y=120,height=40,width=100)
win.mainloop()