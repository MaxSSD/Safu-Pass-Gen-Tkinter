from tkinter import *
import random
import requests

me = Tk()
me.title("Password Generator")
me.geometry("200x140")
me.resizable(False,False)
melabel=Label(me, text="SAFU Password",bg='brown1',font=("Times",18, 'bold'))
melabel.place(y=0,x=0,width=200,height=40)
me.config(background='White')
textin = StringVar()

def password_generator():
    low = "abcdefghijklmnopqrstuvwxyz"
    up = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    num = "0123456789"
    sym = "!@#$%^&*(){}:;<>.,/?"
    all_keys = low + up + num + sym
    pass_len = 18
    password = "".join(random.sample(all_keys, pass_len))
    password += random.choice(all_keys)
    textin.set(password)

but_choice=Button(me,padx=15,pady=-30,bd=0,bg='green3',text="Generate password",command=password_generator,font=("Times new roman",15,'bold'))
but_choice.place(x=0,y=70,width=200,height=70)

display=Entry(me, text='Your answer',textvar=textin,width=25,bd=0,bg='brown1',font=("Courier New",12,'bold'), state="readonly")
display.place(x=0,y=40,width=200,height=30)

password_generator()

me.mainloop()
