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
from PIL import ImageTk, Image

#Variables for the connection with the database
global server , database
server = 'localhost'
database = 'Db_prueba_py'

#Return Main_Window
def return_main():
    welcomeWindow.destroy()
    Main_Window()
    
#Verification of credentials to log in      
def login_verification():
    username = usernameEntry.get()
    password = passwordEntry.get()
    try:
        with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
            cursor = cnxn.cursor()
            cursor.execute("SELECT * FROM Users WHERE UserName=? AND Pass=?", (username, password))
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
    if pass1 != valipass or pass2 != valipass:
        if pass1 == pass2:
            try:
                with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
                    cursor = cnxn.cursor()
                    query = "UPDATE Users SET Email = ?, SecurityQuestion = ?, Pass=? WHERE UserName = ?"
                    
                    cursor.execute(query, (valicorreo, valisq, pass1,valiuser))
                    cnxn.commit
                    messagebox.showinfo("New Password", "The new password was created successfully")
                    newpasswin.destroy()
                    Forgotwindow.destroy()              
            except pyodbc.Error as e:
                messagebox.showerror("ERROR", f"Database error: {e}")
        else:
            messagebox.showerror("Error","Passwords are not equals")
    else:
        messagebox.showerror("Error","I can't use the old password")

#Verification of credentials to register
def register_verification():
    new_username = newuserEntry.get()
    new_email = EmailEntry.get()
    new_secure_q = SecuereQuesEntry.get()
    new_password = passwordEntrys.get()
    if len(new_username) == 0 and len(new_email) == 0 and len(new_secure_q) == 0 and len(new_password) == 0:
        messagebox.showerror("Error","Please fill in all data")
    else:
        if "@" not in new_email:
            messagebox.showerror("Error","The Email not is valid")
        else:
            try:
                with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
                    cursor = cnxn.cursor()
                    cursor.execute("SELECT * FROM Users WHERE UserName=? OR Email=?", (new_username,new_email))
                    if cursor.fetchone() is not None:
                        messagebox.showerror("Register", "User or Email already exists in the System")
                    else:               
                        cursor = cnxn.cursor()
                        regquery = "INSERT INTO Users (UserName, Email, SecurityQuestion, Pass) VALUES (?, ?, ?, ?)"
                        cursor.execute(regquery,new_username,new_email,new_secure_q,new_password)            
                        cnxn.commit()
                        cnxn.close
                        messagebox.showinfo("Register", "Successful Register")
            except pyodbc.Error as e:
                messagebox.showerror("ERROR", f"Database error: {e}")
        
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
        newpasswin.configure(bg="light blue")
        labeln = Label(newpasswin, text="New Password",bg="light blue",fg="SkyBlue4", font=("Courier New", 15, "bold") )
        labeln.place(x=80,y=13)
        newLabel1 = Label(newpasswin, text="New Password",bg="light blue",fg="gray25", font=("Candara", 12, "bold") )
        newLabel1.place(x=100, y=50)    
        newEntry1 = Entry(newpasswin , fg="gray25", font=("Candara", 10, "bold") )
        newEntry1.place(x=80, y=80)     
        passwordLabel = Label(newpasswin, text="Confirm Password",bg="light blue",fg="gray25", font=("Candara", 12, "bold") )
        passwordLabel.place(x=85, y=110)    
        newEntry2 = Entry(newpasswin , fg="gray25", font=("Candara", 10, "bold") )
        newEntry2.place(x=80, y=140)
        changeButton = Button(newpasswin, text="Create New Passord", bg="forest green",fg="white" ,font=("Courier", 10, "bold"), command=validate_new_password)
        changeButton.place(x=70, y=190)
        newpasswin.mainloop()
            
#Principal window       
def Main_Window():
    global tkWindow, usernameEntry, passwordEntry , newuserEntry,EmailEntry,SecuereQuesEntry,passwordEntrys
    tkWindow = Tk()
    tkWindow.title("RHSystem-Workers Admistrator")
    img = Image.open("C://Users//LuisM//OneDrive//Escritorio//GithubCarpets//SystemRH-Workers-Admistrator//Images//login-backround.jpg")
    resized_img = img.resize((600, 550))
    bg_img = ImageTk.PhotoImage(resized_img)
    canvas = Canvas(tkWindow, width=600, height=550)
    canvas.pack()
    canvas.create_image(0, 0, image=bg_img, anchor=NW)
    tkWindow.resizable(0,0)
    labelprincipal = Label(tkWindow, text="RH-System",bg="light blue",fg="SkyBlue4", font=("Times New Roman", 30, "bold") )
    labelprincipal.place(x=220,y=30)
    labellogin = Label(tkWindow, text="Login Validation",bg="light blue",fg="SkyBlue4", font=("Courier New", 15, "bold") )
    labellogin.place(x=70,y=110)
    labelreg = Label(tkWindow, text="Register User",bg="light blue",fg="SkyBlue4", font=("Courier New", 15, "bold") )
    labelreg.place(x=400,y=110)
    usernameLabel = Label(tkWindow, text="Username",bg="light blue",fg="gray25", font=("Candara", 12, "bold") )
    usernameLabel.place(x=120, y=170)    
    usernameEntry = Entry(tkWindow,fg="gray25", font=("Candara", 10, "bold") )
    usernameEntry.place(x=90, y=210)     
    passwordLabel = Label(tkWindow, text="Password",bg="light blue",fg="gray25", font=("Candara", 12, "bold") )
    passwordLabel.place(x=120, y=240)    
    passwordEntry = Entry(tkWindow, show='*' , fg="gray25", font=("Candara", 10, "bold") )
    passwordEntry.place(x=90, y=280)
    usernameLabel = Label(tkWindow, text="New Username",bg="light blue",fg="gray25", font=("Candara", 12, "bold"))
    usernameLabel.place(x=425, y=160)
    newuserEntry = Entry(tkWindow,fg="gray25", font=("Candara", 10, "bold") )
    newuserEntry.place(x=405, y=200)
    EmailLabel = Label(tkWindow, text="New Email",bg="light blue",fg="gray25", font=("Candara", 12, "bold"))
    EmailLabel.place(x=435, y=240)
    EmailEntry = Entry(tkWindow,fg="gray25", font=("Candara", 10, "bold") )
    EmailEntry.place(x=405, y=280)
    SecuereQuesLabel = Label(tkWindow, text="You Birth town",bg="light blue",fg="gray25", font=("Candara", 12, "bold"))
    SecuereQuesLabel.place(x=425, y=310)    
    SecuereQuesEntry = Entry(tkWindow,fg="gray25", font=("Candara", 10, "bold") )
    SecuereQuesEntry.place(x=405, y=350)          
    passwordLabel = Label(tkWindow, text="New Password",bg="light blue",fg="gray25", font=("Candara", 12, "bold"))
    passwordLabel.place(x=425, y=390)    
    passwordEntrys = Entry(tkWindow, show='*',fg="gray25", font=("Candara", 10, "bold") )
    passwordEntrys.place(x=405, y=430)           
    loginButton = Button(tkWindow, text="Login", width=10, height=1, bg="forest green" , fg="white" ,font=("Courier", 10, "bold") , command=login_verification) 
    loginButton.place(x=110, y=315)
    regButton = Button(tkWindow, text="Register User +", width=15, height=1, bg="midnight blue",fg="white" ,font=("Courier", 10, "bold"),command=register_verification)
    regButton.place(x=408, y=470)
    RememberButton = Button(tkWindow, text="Forgot your password", width=20, height=1, bg="firebrick4",fg="white" ,font=("Courier", 10, "bold"), command=Forgot_password_window)
    RememberButton.place(x=75, y=360)   
    tkWindow.mainloop()
    

#Forgot password window
def Forgot_password_window():
    global Forgotwindow, codeEntry, secretcode , valiuser,valicorreo,valisq, valipass
    #Get username data input
    gets_username = usernameEntry.get()
    if len(gets_username) == 0:
        messagebox.showerror("Error","Please fill in the information to help you")
    else:
        #forgot window database connection
        try:
            with pyodbc.connect(f"DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;") as cnxn:
                cursor = cnxn.cursor()
                cursor.execute("SELECT * FROM Users WHERE UserName=?", (gets_username))
                for row in cursor.fetchall():
                    valiuser = row[0]
                    valicorreo = row[1]
                    valisq = row[2]
                    valipass = row[3]
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
        msg['Subject'] = 'Code to change password'
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('soportprimeprogram@gmail.com', 'lgvozquxlykfijaq')
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
    opb6 = Button(welcomeWindow, text="Exit", width=20, height=3, bg="dark green",fg="white",command=return_main)
    opb6.place(x=340, y=140)
    welcomeWindow.mainloop()

#Talk principal function 
Main_Window()