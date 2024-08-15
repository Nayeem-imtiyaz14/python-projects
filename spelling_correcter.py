from tkinter import *
from textblob import TextBlob
def correct_spelling():
    get_data=enter1.get()
    cor=TextBlob(get_data)
    data=cor.correct()
    enter2.delete(0,END)
    enter2.insert(0,data)
win=Tk()
global enter1,enter2
win.geometry("500x500")
win.title("WEATHER APP")
win.config(bg="gray")
label1=Label(win,text="Incorrect Spelling",font=("Time New Roman",20,"bold"))
label1.place(x=20,y=80,height=50,width=450)
enter1=Entry(win,font=("Time New Roman",20))
enter1.place(x=67,y=150,height=40,width=300)
label2=Label(win,text="Correct Spelling",font=("Time New Roman",20,"bold"))
label2.place(x=20,y=210,height=50,width=450)
enter2=Entry(win,font=("Time New Roman",20))
enter2.place(x=67,y=280,height=40,width=300)
button1=Button(win,text="Done",font=("Time New Roman",20,"bold"),command=correct_spelling)
button1.place(x=200,y=340,height=30,width=80)
win.mainloop()