from tkinter import *
import os
import ml
# Designing window for login 
 
def login():
    main_screen.withdraw()
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("400x400")
    login_screen.config(bg="cornflowerblue")
    #Label(login_screen, text="Enter details to Signin",font=("Bold",13),bg="cornflowerblue").grid(padx=25)
    #Label(login_screen, text="",width="0",height="2",bg="cornflowerblue").grid(row=1,column=0)
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ",font=("Bold",13)).grid(row=0,column=0,padx=30,pady=40)
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.grid(row=0,column=1,padx=20,pady=40)
    #Label(login_screen, text="",width="0",height="3",bg="cornflowerblue").grid(row=3)
    Label(login_screen, text="Password * ",font=("Bold",13)).grid(row=4,column=0,padx=30,pady=30)
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.grid(row=4,column=1,padx=20)
    #Label(login_screen, text="",width="0",height="4",bg="cornflowerblue").grid(row=5)
    Button(login_screen, text="Login", width="10", height="1", command = login_verify,font=("Bold",13),bg="CadetBlue4").grid(padx=30,pady=30)
 
# Designing window for registration
 
def register():
    #main_screen.withdraw()
    global register_screen
    global login
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("400x400")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="grey").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width="10", height="1", bg="grey", command = register_user).pack()
    Label(register_screen,text="").pack()
    Button(register_screen, text="Login", width="10", height="1",bg="grey", command = login).pack()

 

# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
    
    
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
    #login_screen.destroy()
 
# Designing popup for login success
 
def Diebetes():
    import diabetes_gui

def login_sucess():
    login_screen.withdraw()
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("400x400")
    Button(login_success_screen, text="Diabtetes Test",command=Diebetes).pack()
# Designing popup for login invalid password

def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("400x400")
    main_screen.config(bg ="midnight blue")
    main_screen.title("Account Login")
    #Label(text="SELECT YOUR CHOICE", bg="antique white", width="300", height="2", font=("Bold", 13)).pack()
    Label(main_screen,text="",height="4",width="0",bg="midnight blue").pack()
    
    login_but=Button(main_screen,text="LOGIN", height="2", width="30", command = login,font=("Bold",13)).pack()
    Label(main_screen,text="",height="4",width="0",bg="midnight blue").pack()
    Button(main_screen,text="REGISTER", height="2", width="30", command=register,font=("Bold",13)).pack()
 
    main_screen.mainloop()
 
 
main_account_screen()      
