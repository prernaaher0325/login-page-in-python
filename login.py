from tkinter import *
import os
from tkinter import messagebox

def register_user():
    username_info = username.get()
    password_info = password.get()


    file = open(username_info,'w')
    file.write(username_info+'\n')
    file.write(password_info)
    file.close()
    Label(screen1,text="Registeration Success",font ="green",height='2', width='20').pack()

def verify():
        username1 = username_verify.get()
        password1 = password_verify.get()


        os_list = os.listdir()
        if username1 in os_list:
            file = open(username1,'r')
            v = file.read().split()
            if password1 in v:
                messagebox.showinfo('success',"Login Success")
            else:
                messagebox.showinfo('not found',"Password is wrong")


        else:
            messagebox.showinfo('no user','Please register you')
def login():
    pass
    global screen2
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    screen2= Toplevel(screen)
    screen2.geometry("500x300")
    screen2.title("login")
    Label(screen2,text='login').pack()
    Label(screen2,text='username').pack()
    Entry(screen2,textvariable= username_verify).pack()
    Label(screen2,text="password").pack()
    Entry(screen2,textvariable= password_verify).pack()

    Label(screen2,text= "").pack()
    Button(screen2,text='Login', height=2, width=15, command=verify).pack()
    
    

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("390x290")
    screen1.title("register")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1,text= 'Fill all details to register').pack()
    Label(screen1,text= "").pack()
    Label(screen1,text = "username").pack()
    username_entry= enter= Entry(screen1,textvariable=username).pack()
    Label(screen1,text= "").pack()

    Label(screen1,text = "Password").pack()
    password_entry= enter= Entry(screen1,textvariable=password).pack()
    Label (screen1,text="").pack()
    Button(screen1,text='Register',height= 3, width=15,command= register_user).pack()    
    
    



    
def main():
    global screen
    screen = Tk()
    screen.geometry('400x400')
    Label(text='Longin Form').pack()
    Button(text="login",height = 3,width=15, command= login).pack()
    Button(text="register", height = 3,width=15, command= register).pack()




    screen.mainloop()

main()


