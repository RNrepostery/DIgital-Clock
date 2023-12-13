from tkinter import *
from time import strftime
m=Tk()
def clock():
    l1["text"]=strftime("%I:%M:%S %p")
    l1.after(1000,clock)

def Digitalclock():
    l2["text"]=strftime("%a : %d : %b %Y")
f=Frame(m,relief="solid")
f.pack(fill=BOTH)    
        
l1=Label(f,text="12:25:37 AM",font=("digital-7",35,"bold"),bg="black",fg="white",relief='flat')
l1.pack(fill=BOTH)
l2=Label(f,text="Wed, 01 Feb 2023",font=("digital-7",35,"bold"),bg="black",fg="white")
l2.pack(fill=BOTH)
l=Label(f,text="Developed by Rohit ",font=("Palace Script MT",35,"bold"),bg="black",fg="white")
l.pack(fill=BOTH)

clock()
Digitalclock()
mainloop()