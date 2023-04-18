#Imported Libraries
from tkinter import *
import tkinter.messagebox as messagebox
from tkinter import messagebox
import random
import string
from email.message import EmailMessage
import smtplib
import messagebox
from datetime import date
import pyodbc
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Imported Variables the Security.py
from Security import secretcode , Email_Master_User, Email_Master_Password,server,database,html

#Function of Principal window
def Main_Window():
    global tkWindow, usernameEntry, passwordEntry,  EmailEntry
    tkWindow = Tk()
    tkWindow.title("RHSystem-Workers Admistrator")
    tkWindow.geometry("400x450")
    tkWindow.configure(bg="light blue")
    tkWindow.resizable(0, 0)
    labelprincipal = Label(tkWindow, text="RH-System", bg="light blue",fg="SkyBlue4", font=("Times New Roman", 30, "bold"))
    labelprincipal.place(x=100, y=30)
    labellogin = Label(tkWindow, text="Login Validation", bg="light blue",fg="SkyBlue4", font=("Courier New", 15, "bold"))
    labellogin.place(x=100, y=100)
    usernameLabel = Label(tkWindow, text="Username", bg="light blue",fg="gray25", font=("Candara", 12, "bold"))
    usernameLabel.place(x=70, y=150)
    usernameEntry = Entry(tkWindow, fg="gray25", font=("Candara", 12, "bold"))
    usernameEntry.place(x=10, y=180)
    passwordLabel = Label(tkWindow, text="Password", bg="light blue",fg="gray25", font=("Candara", 12, "bold"))
    passwordLabel.place(x=250, y=150)
    passwordEntry = Entry(tkWindow, show='*', fg="gray25",font=("Candara", 12, "bold"))
    passwordEntry.place(x=210, y=180)
    loginButton = Button(tkWindow, text="Login", width=10, height=1, bg="forest green",fg="white", font=("Courier", 13, "bold"), command=login_verification)
    loginButton.place(x=145, y=240)
    RememberButton = Button(tkWindow, text="Forgot your password", width=21, height=1,bg="firebrick4", fg="white", font=("Courier", 13, "bold"), command=Forgot_password_window)
    RememberButton.place(x=95, y=310)
    tkWindow.mainloop()

# Function to login in the system
def login_verification():
    username = usernameEntry.get()
    password = passwordEntry.get()
    if len(username) == 0 and len(password) == 0:
        messagebox.showerror("Error", "Please fill in all data")
    else:
        try:
            with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
                cursor = cnxn.cursor()
                cursor.execute(
                    "SELECT * FROM Users WHERE UserName=? AND Pass=?", (username, password))
                if cursor.fetchone() is not None:
                    messagebox.showinfo("LOGIN", "Successful login")
                    tkWindow.destroy()
                    welcome_window()
                else:
                    messagebox.showerror("LOGIN", "Incorrect login")
        except pyodbc.Error as e:
            messagebox.showerror("ERROR", f"Database error: {e}")

# Test window
def welcome_window():
    global welcomeWindow
    welcomeWindow = Tk()
    welcomeWindow.title("Welcome")
    welcomeWindow.geometry("510x500")
    welcomeWindow.resizable(0, 0)
    welcomeWindow.configure(bg="dark slate gray")
    Label(welcomeWindow, text="RH System Administrator",width="300", height=2, bg="gray25", fg="white").pack()
    opb1 = Button(welcomeWindow, text="Workers Availables",width=20, height=3, bg="dark green", fg="white")
    opb1.place(x=20, y=60)
    opb2 = Button(welcomeWindow, text="Consult Workers",width=20, height=3, bg="dark green", fg="white")
    opb2.place(x=180, y=60)
    opb3 = Button(welcomeWindow, text="Change Data Workers",width=20, height=3, bg="dark green", fg="white")
    opb3.place(x=340, y=60)
    opb4 = Button(welcomeWindow, text="Send an email to worker",width=20, height=3, bg="dark green", fg="white")
    opb4.place(x=20, y=140)
    opb5 = Button(welcomeWindow, text="Add New Worker", width=20,height=3, bg="dark green", fg="white")
    opb5.place(x=180, y=140)
    opb6 = Button(welcomeWindow, text="Exit", width=20, height=3,bg="dark green", fg="white", command=return_main)
    opb6.place(x=340, y=140)
    welcomeWindow.mainloop()

# Function to return to the main window
def return_main():
    welcomeWindow.destroy()
    Main_Window()

#Function of the take email window
def Forgot_password_window():
    global EmailEntry,forgot_window_1
    forgot_window_1 = Tk()
    forgot_window_1.title("RHSystem-Forgot Password")
    forgot_window_1.geometry("400x300")
    forgot_window_1.configure(bg="light blue")
    forgot_window_1.resizable(0, 0)
    labelprincipal = Label(forgot_window_1, text="RH-System", bg="light blue",fg="SkyBlue4", font=("Times New Roman", 30, "bold"))
    labelprincipal.place(x=110, y=30)
    labellogin = Label(forgot_window_1, text="Forgot-Password-Security",bg="light blue", fg="SkyBlue4", font=("Courier New", 15, "bold"))
    labellogin.place(x=60, y=100)
    usernameLabel = Label(forgot_window_1, text="Enter your Email Adress",bg="light blue", fg="gray25", font=("Candara", 12, "bold"))
    usernameLabel.place(x=130, y=150)
    EmailEntry = Entry(forgot_window_1, fg="gray25",font=("Candara", 12, "bold"))
    EmailEntry.place(x=110, y=180)
    EmailButton = Button(forgot_window_1, text="Validate Email", width=15, height=1,bg="forest green", fg="white", font=("Courier", 13, "bold"), command=validateEmail)
    EmailButton.place(x=120, y=220)
    forgot_window_1.mainloop()

#Function to validate email, send code and get code window
def validateEmail():
    global codeEntry, secretcode, takeemail,Forgotwindow
    takeemail = EmailEntry.get()
    if len(takeemail) == 0 or "@" not in takeemail:
        messagebox.showerror("Error", "Please enter your correct email adress")
    else:
        # Validate the email in the system
        messagebox.showinfo("Success", "Checking if Email is in the system")
        try:
            with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
                cursor = cnxn.cursor()
                cursor.execute( "SELECT * FROM Users WHERE Email=?", (takeemail))
                if cursor.fetchone() is not None:
                    messagebox.showinfo("Success", "Email found in the system")
                    messagebox.showinfo("Success", "Please check your email for the security code")
                    forgot_window_1.destroy()
                    # Window to get the secret code
                    Forgotwindow = Tk()
                    Forgotwindow.title("Forgot your Password")
                    Forgotwindow.geometry("400x300")
                    Forgotwindow.configure(bg="light blue")
                    Forgotwindow.resizable(0, 0)
                    labelprincipal = Label(Forgotwindow, text="RH-System", bg="light blue",fg="SkyBlue4", font=("Times New Roman", 30, "bold"))
                    labelprincipal.place(x=110, y=30)
                    codeLabel = Label(Forgotwindow, text="Verificate your Code:",bg="light blue", fg="SkyBlue4", font=("Courier New", 15, "bold"))
                    codeLabel.place(x=80, y=100)
                    code1Label = Label(Forgotwindow, text="Enter your secret code here",bg="light blue", fg="gray25", font=("Candara", 12, "bold"))
                    code1Label.place(x=100, y=150)
                    codeEntry = Entry(Forgotwindow, fg="gray25", font=("Candara", 12, "bold"))
                    codeEntry.place(x=100, y=180)
                    validateButton = Button(Forgotwindow, text="Validate Code", width=15, height=1, bg="forest green", fg="white", font=("Courier", 13, "bold"),command=new_password)
                    validateButton.place(x=110, y=220)                    
                    # Process to send the email
                    msg = MIMEMultipart()
                    msg.attach(MIMEText(html, 'html'))
                    msg['From'] = Email_Master_User
                    msg['To'] = takeemail
                    msg['Subject'] = 'Code to change password'
                    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                        smtp.starttls()
                        smtp.login(Email_Master_User,Email_Master_Password)
                        smtp.send_message(msg)
                    Forgotwindow.mainloop()
                else:
                    messagebox.showerror("Error", "Email not found in the system")
        except pyodbc.Error as e:
            messagebox.showerror("ERROR", f"Database error: {e}")

# Function to create a new password window
def new_password():
    global newpasswin, newEntry1, newEntry2
    codes = codeEntry.get()
    if codes == secretcode:
        messagebox.showinfo("Validate", "The data is correct")
        Forgotwindow.destroy()
        newpasswin = Tk()
        newpasswin.title("Create New Password")
        newpasswin.geometry("400x350")
        newpasswin.resizable(0, 0)
        newpasswin.configure(bg="light blue")
        labelprincipal = Label(newpasswin, text="RH-System", bg="light blue",fg="SkyBlue4", font=("Times New Roman", 30, "bold"))
        labelprincipal.place(x=110, y=30)
        labeln = Label(newpasswin, text="Create New Password", bg="light blue",fg="SkyBlue4", font=("Courier New", 15, "bold"))
        labeln.place(x=90, y=100)
        newLabel1 = Label(newpasswin, text="New Password",bg="light blue",fg="gray25", font=("Candara", 12, "bold"))
        newLabel1.place(x=50, y=140)
        newEntry1 = Entry(newpasswin, fg="gray25",font=("Candara", 12, "bold"))
        newEntry1.place(x=10, y=170)
        passwordLabel = Label(newpasswin, text="Confirm Password",bg="light blue", fg="gray25", font=("Candara", 12, "bold"))
        passwordLabel.place(x=230, y=140)
        newEntry2 = Entry(newpasswin, fg="gray25",font=("Candara", 12, "bold"))
        newEntry2.place(x=210, y=170)
        changeButton = Button(newpasswin, text="Confirm New Password", width=20, height=1,bg="forest green", fg="white", font=("Courier", 13, "bold"),command=validate_new_password)
        changeButton.place(x=100, y=230)
        newpasswin.mainloop()

# Function to create a new password and replace the old one.
def validate_new_password():
    pass1 = newEntry1.get()
    pass2 = newEntry2.get()
    #Check that the data entered are the same
    if pass1 != pass2:
        messagebox.showerror("Error", "Passwords are not equals")
    else:
        try:
            #Take the user data with his email address
            with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
                cursor = cnxn.cursor()
                cursor.execute("SELECT * FROM Users WHERE Email=?", (takeemail))
                for row in cursor.fetchall():
                    valiuser = row[0]
                    valicorreo = row[1]
                    valisq = row[2]
                    valipass = row[3]
        except pyodbc.Error as e:
            messagebox.showerror("ERROR", f"Database error: {e}")
        #Check that the new password is not the same as the old one            
        if pass1 != valipass or pass2 != valipass:
            try:
                #Update the new password
                with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
                    cursor = cnxn.cursor()
                    query = "UPDATE Users SET Email = ?, SecurityQuestion = ?, Pass=? WHERE UserName = ?"
                    cursor.execute(query, (valicorreo, valisq, pass1, valiuser))
                    cnxn.commit
                    messagebox.showinfo("New Password", "The new password was created successfully")
                    newpasswin.destroy()
            except pyodbc.Error as e:
                messagebox.showerror("ERROR", f"Database error: {e}")
        else:
            messagebox.showerror("Error", "I can't use the old password")

# Talk principal function
Main_Window()