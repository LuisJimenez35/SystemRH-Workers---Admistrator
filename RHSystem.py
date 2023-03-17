#Imported Libraries
from tkinter import *
import tkinter.messagebox as messagebox
import random
import string
from email.message import EmailMessage
import smtplib
import messagebox
from datetime import date
import pyodbc
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Variables for the connection with the database
global server , database
server = 'localhost'
database = 'Db_prueba_py'

#Return principal #1
def return_principal():
    reisterw.destroy()
    principal_window()  
#Return principal #2
def return_principal_2():
    tkWindow.destroy()
    principal_window()
#Return principal #3
def return_principal_3():
    welcomeWindow.destroy()
    principal_window()
#Close project
def close_project():
    rootw.destroy()

#Verification of credentials to log in      
def login_verification():
    username = usernameEntry.get()
    password = passwordEntry.get()
    try:
        with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM users WHERE UserName=? AND Pass=?", (username, password))
            if cursor.fetchone() is not None:
                messagebox.showinfo("LOGIN", "Successful login")
                tkWindow.destroy()
                welcome_window()                
            else:
                messagebox.showerror("LOGIN", "Incorrect login")
    except pyodbc.Error as e:
        messagebox.showerror("ERROR", f"Database error: {e}")

#Validate update password
def validate_new_password():
    pass1 = newEntry1.get()
    pass2 = newEntry2.get()
    if pass1 == pass2:
        try:
            with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
                cursor = cnxn.cursor()
                query = "UPDATE users SET Email = ?, SecurityQuestion = ?, Pass=? WHERE UserName = ?"
                
                cursor.execute(query, (valicorreo, valisq, pass1,valiuser))
                cnxn.commit
                messagebox.showinfo("New Password", "The new password was created successfully")
                newpasswin.destroy()
                Forgotwindow.destroy()              
        except pyodbc.Error as e:
            messagebox.showerror("ERROR", f"Database error: {e}")
    else:
        messagebox.showerror("Error","Passwords are not equals")

#Create new password window 
def new_password():
    global newpasswin, newEntry1, newEntry2
    codes = codeEntry.get()
    if codes == secretcode:
        messagebox.showinfo("Validate","The data is correct")
        newpasswin = Tk()
        newpasswin.title("Create New Password")
        newpasswin.geometry("300x250")
        newpasswin.resizable(0,0)
        newpasswin.configure(bg="dark slate gray")
        Label(newpasswin, text="Please enter all details", width="300",height=2, bg="dark green",fg="white").pack()
        newLabel1 = Label(newpasswin, text="New Password",bg="dark slate gray",fg="white")
        newLabel1.place(x=30, y=50)    
        newEntry1 = Entry(newpasswin)
        newEntry1.place(x=100, y=50)     
        passwordLabel = Label(newpasswin, text="Confirm Password",bg="dark slate gray",fg="white")
        passwordLabel.place(x=30, y=80)    
        newEntry2 = Entry(newpasswin)
        newEntry2.place(x=100, y=80)
        changeButton = Button(newpasswin, text="Create New Passord", width=10, height=1, bg="forest green", command=validate_new_password)
        changeButton.place(x=50, y=130)
        newpasswin.mainloop()
        
#Verification of credentials to register
def register_verification():
    new_username = newuserEntry.get()
    new_email = EmailEntry.get()
    new_secure_q = SecuereQuesEntry.get()
    new_password = passwordEntry.get()
    try:
        with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM users WHERE UserName=?", (new_username))
            if cursor.fetchone() is not None:
                messagebox.showerror("Register", "User already exists")
                reisterw.destroy()
                principal_window()
            else:               
                cursor = cnxn.cursor()
                regquery = "INSERT INTO users (UserName, Email, SecurityQuestion, Pass) VALUES (?, ?, ?, ?)"
                cursor.execute(regquery,new_username,new_email,new_secure_q,new_password)            
                cnxn.commit()
                cnxn.close
                messagebox.showinfo("Register", "Successful Register")
                reisterw.destroy()
                principal_window()
    except pyodbc.Error as e:
        messagebox.showerror("ERROR", f"Database error: {e}")
    
#Welcome and main window
def principal_window():
    global rootw
    rootw = Tk()
    rootw.title("RHSystem")
    rootw.geometry("300x250")
    rootw.configure(bg="dark slate gray")
    rootw.resizable(0,0)
    Label(rootw, text="Please enter details below", width="300",height=2, bg="gray25",fg="white").pack()  
    loginw = Button(rootw, text="Log-in", width=13, height=2, bg="dark green",fg="white", command=login_window)
    loginw.place(x=100, y=60)
    regw = Button(rootw, text="Sign-up", width=13, height=2, bg="blue4",fg="white", command=register_window)
    regw.place(x=100, y=120)
    stopw = Button(rootw, text="Quit X", width=10, height=2, bg="brown4",fg="white", command=close_project)
    stopw.place(x=110, y=180)      
    rootw.mainloop()
    
#Login window       
def login_window():
    rootw.destroy()   
    global tkWindow, usernameEntry, passwordEntry
    tkWindow = Tk()
    tkWindow.title("Login Form")
    tkWindow.geometry("300x230")
    tkWindow.resizable(0,0)
    tkWindow.configure(bg="dark slate gray")
    Label(tkWindow, text="Please enter all details", width="300",height=2, bg="dark green",fg="white").pack()
    usernameLabel = Label(tkWindow, text="Username",bg="dark slate gray",fg="white")
    usernameLabel.place(x=30, y=50)    
    usernameEntry = Entry(tkWindow)
    usernameEntry.place(x=100, y=50)     
    passwordLabel = Label(tkWindow, text="Password",bg="dark slate gray",fg="white")
    passwordLabel.place(x=30, y=80)    
    passwordEntry = Entry(tkWindow, show='*')
    passwordEntry.place(x=100, y=80)
    loginButton = Button(tkWindow, text="Login", width=10, height=1, bg="forest green", command=login_verification)
    loginButton.place(x=50, y=130)
    RememberButton = Button(tkWindow, text="Forgot your password", width=16, height=1, bg="firebrick4", fg="white" , command=Forgot_password_window)
    RememberButton.place(x=150, y=130)
    retButton = Button(tkWindow, text="<- Return Menu", width=14, height=1, bg="PaleGreen4", command=return_principal_2)
    retButton.place(x=95, y=180)      
    tkWindow.mainloop()

#Register window   
def register_window():
    rootw.destroy()
    global reisterw,newuserEntry,EmailEntry,SecuereQuesEntry,passwordEntry
    reisterw = Tk()
    reisterw.title("Register new RH-User")
    reisterw.geometry("300x320")
    reisterw.configure(bg="dark slate gray")
    reisterw.resizable(0,0)
    Label(reisterw, text="Please enter all details", width="300",height=2, bg="midnight blue",fg="white").pack()  
    usernameLabel = Label(reisterw, text="New Username",bg="dark slate gray",fg="white")
    usernameLabel.place(x=22, y=50)    
    newuserEntry = Entry(reisterw)
    newuserEntry.place(x=110, y=50)    
    EmailLabel = Label(reisterw, text="New Email",bg="dark slate gray",fg="white")
    EmailLabel.place(x=22, y=90)    
    EmailEntry = Entry(reisterw)
    EmailEntry.place(x=110, y=90)   
    SecuereQuesLabel = Label(reisterw, text="You Birth town",bg="dark slate gray",fg="white")
    SecuereQuesLabel.place(x=22, y=130)    
    SecuereQuesEntry = Entry(reisterw)
    SecuereQuesEntry.place(x=110, y=130)          
    passwordLabel = Label(reisterw, text="New Password",bg="dark slate gray",fg="white")
    passwordLabel.place(x=22, y=170)    
    passwordEntry = Entry(reisterw, show='*')
    passwordEntry.place(x=110, y=170)        
    regButton = Button(reisterw, text="Register User +", width=15, height=2, bg="midnight blue",fg="white", command=register_verification)
    regButton.place(x=107, y=220)
    returnButton = Button(reisterw, text="<- Return Menu", width=12, height=1, bg="PaleGreen4",fg="white",command=return_principal)
    returnButton.place(x=115, y=270)   
    reisterw.mainloop()

#Forgot password window
def Forgot_password_window():
    global Forgotwindow, codeEntry, secretcode , valiuser,valicorreo,valisq
    #Get username data input
    gets_username = usernameEntry.get()
    #forgot window database connection
    try:
        with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM users WHERE UserName=?", (gets_username))
            for row in cursor.fetchall():
                valiuser = row[0]
                valicorreo = row[1]
                valisq = row[2]
                valipass = row[3]
                print(valicorreo)
    except pyodbc.Error as e:
        messagebox.showerror("ERROR", f"Database error: {e}")
    ##Create a secret code
    caracters = string.ascii_letters + string.digits
    longitud = 6
    secretcode = ''.join(random.choice(caracters) for _ in range(longitud))
    #HTML and css format for sending the secret code email
    html = """\
    <html>
    <head></head>
    <body style="background-image: url(NewProject/images/fondo-verde-borroso-de-la-luz-del-extracto-bokeh-brillo-102747021.jpg); background-position: center;">
        <div class="card" style="margin: 0 auto; text-align: center; align-items: center; background-color: rgb(255, 255, 255); width: 70%; height: 280px; margin-top: 10%;">
            <br>
            <h2 style="text-align: start; margin-left: 10%; margin-top: 5; font-size: 123%; color: blue;" >RHSystem/LuisJimenez35</h2>
            <h3 style="margin-top: 30px; display: inline-block; text-align: center; color: rgb(7, 7, 7); font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif ; font-weight: bold; font-size: 140%;">Hello, please enter the following code to recover your password</h3>
            <br>
            <hr>
            <h1 style="color: rgb(51, 94, 214); font-size: 300%; position: relative; top: auto;">"""+secretcode+"""</h1>
        </div>
    </body>
    </html>
    """
    #Process to send the email
    msg = MIMEMultipart()
    msg.attach(MIMEText(html, 'html'))
    msg['From'] = 'soportprimeprogram@gmail.com'
    msg['To'] = valicorreo
    msg['Subject'] = 'Codigo para cambiar password'
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('soportprimeprogram@gmail.com', 'gbaabtuzmxgxrvhn')
        smtp.send_message(msg)
    Forgotwindow = Tk()
    Forgotwindow.title("Forgot your Password")
    Forgotwindow.geometry("300x230")
    Forgotwindow.configure(bg="dark slate gray")
    Forgotwindow.resizable(0,0)
    Label(Forgotwindow, text="Forgot Password Vent", width="300",height=1, bg="gray25",fg="white").pack()
    Codelabel = Label(Forgotwindow, text="A code has just been sent to your email.",bg="dark green",fg="white")
    Codelabel.place(x=45, y=40)
    codeLabel = Label(Forgotwindow, text="Put the code sent here:",bg="dark slate gray",fg="white")
    codeLabel.place(x=90, y=80)    
    codeEntry = Entry(Forgotwindow)
    codeEntry.place(x=90, y=105)
    validateButton = Button(Forgotwindow, text="Validate Code", width=11, height=1, bg="forest green",fg="white" , command=new_password)
    validateButton.place(x=105, y=150)     
    Forgotwindow.mainloop()
    
#Test window
def welcome_window():
    global welcomeWindow
    welcomeWindow = Tk()
    welcomeWindow.title("Welcome")
    welcomeWindow.geometry("510x500")
    welcomeWindow.resizable(0,0)
    welcomeWindow.configure(bg="dark slate gray")
    Label(welcomeWindow, text="RH System Administrator", width="300",height=2, bg="gray25",fg="white").pack()
    opb1 = Button(welcomeWindow, text="Workers Availables", width=20, height=3, bg="dark green",fg="white")
    opb1.place(x=20, y=60)
    opb2 = Button(welcomeWindow, text="Consult Workers", width=20, height=3, bg="dark green",fg="white")
    opb2.place(x=180, y=60)
    opb3 = Button(welcomeWindow, text="Change Data Workers", width=20, height=3, bg="dark green",fg="white")
    opb3.place(x=340, y=60)
    opb4 = Button(welcomeWindow, text="Send an email to worker", width=20, height=3, bg="dark green",fg="white")
    opb4.place(x=20, y=140)
    opb5 = Button(welcomeWindow, text="Add New Worker", width=20, height=3, bg="dark green",fg="white")
    opb5.place(x=180, y=140)
    opb6 = Button(welcomeWindow, text="Exit", width=20, height=3, bg="dark green",fg="white",command=return_principal_3)
    opb6.place(x=340, y=140)
    welcomeWindow.mainloop()

#Talk principal function 
principal_window()
