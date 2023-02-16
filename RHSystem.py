import random
import pymysql
from email.message import EmailMessage
import smtplib
import messagebox

#----------------Funcion para crear nueva contraseña-----------------
def olvidopass():
    print("Sistema para cambiar contraseña:\n")
    inputadmin = input("Digite su usuario: ")
    #-----------------Conexion a la Base de datos de los Administradores--------------
    db = pymysql.connect(
            host="localhost",
            user="root",
            passwd="Halobat17.",
            db="rhdb"
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM users where Usuario ='" +inputadmin+ "'")
    for row in cur.fetchall():
        valicorreo = row[1]
        valiuser = row[0]
        valiSQ = row[2]
    #--------------Creador del codigo random secreto-------------
    randlowercase1 = chr(random.randint(ord('a'), ord('z')))
    randuppercase2 = chr(random.randint(ord('A'), ord('Z')))
    randuppercase3 = chr(random.randint(ord('A'), ord('Z')))
    randuppercase4 = chr(random.randint(ord('a'), ord('z')))
    randuppercase5 = chr(random.randint(ord('A'), ord('Z')))
    secretcode = (randlowercase1+randuppercase2+randuppercase3+randuppercase4+randuppercase5)
    #------------Enviar el correo de soporte-----------------
    remit = "soportprimeprogram@gmail.com"
    desto = valicorreo
    msj = "Para crear una contraseña nueva digite el siguiente codigo en el Sistema: "+secretcode
    email = EmailMessage()
    email["From"] = remit
    email["To"] = desto
    email["Subject"] = "Correo de Soporte"
    email.set_content(msj)
    smtp = smtplib.SMTP_SSL("smtp.gmail.com")
    smtp.login(remit, "gbaabtuzmxgxrvhn")
    smtp.sendmail(remit, desto, email.as_string())
    smtp.quit()
    print("Correo Enviado")
    #---------------Actulizar la nueva contraseña----------------
    inputcode = input("Digite el codigo enviado a su correo: ")
    if inputcode == secretcode:
        print("Su codigo es correcto")
        newpass = input("Digite la nueva contraseña: ")
        newpass2 = input("Confirme la contraseña: ")
        if newpass == newpass2:
            newpass3 = newpass
            updated_users = """UPDATE users
                        SET Email = %s,
                            SecurityQuestion = %s,
                            Pass = %s
                        WHERE Usuario = %s;"""
            cur.execute(updated_users, (valicorreo, valiSQ, newpass3, valiuser))
            db.commit()
            print("Contraseña Cambiada con exito")
            login()
    else:
        print("Error , verifique su correo")


#-------------------Funcion conexion la base Trabajadores---------------#
def conexionbasetrabajadores():
    db = pymysql.connect(
        host="localhost",
        user="root",
        passwd="Halobat17.",
        db="rhdb"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM trabajadores")
    for DNI, FullName, FullLastName, Birthday, Location, DateOfHire, Position, Cellphone, Email, Salary in cur.fetchall() :
        print("\nDNI:",DNI, "\nNombre Completo:",FullName, "\nApellidos:",FullLastName, "\nFecha de Nacimiento:",Birthday, "\nUbicacion:",Location, "\nFecha de Contratacion:",DateOfHire, "\nPuesto:",Position, "\nTelefono:",Cellphone, "\nEmail:",Email, "\nSalario:",Salary,)


#-------------------Funcion conexion la base Administradores---------------#
def conexionbaseadmins():
    db = pymysql.connect(
        host="localhost",
        user="root",
        passwd="Halobat17.",
        db="rhdb"
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM users")
    print("Administradores")
    for Usuario, Email in cur.fetchall() :
        print("\nUsuario:",Usuario, "\nEmail:",Email,)


#-------------------Consulta Trabajadores---------------#
def consultardatostrabajadores():
    print("Sistema Recursos Humanos\n")
    db = pymysql.connect(
        host="localhost",
        user="root",
        passwd="Halobat17.",
        db="rhdb"
    )
    opciontrabajador = int(input("{----------Menu----------}\n1.Trabajadores Disponibles\n2.Ver Datos de Trabajadores\n3.Cambiar Correo de Usuarios\n4.Enviar Correo a Trabajador\n5.Agregar Trabajador Trabajador\n6.Eiminar Trabajador\n"))
    #-------------------Cosnultar la Lista de trabajadores general---------------#
    if opciontrabajador == 1:
        print("Trabajadores Disponibles")
        cur = db.cursor()
        cur.execute("SELECT * FROM trabajadores")
        for DNI, FullName, FullLastName, Birthday, Location, DateOfHire, Position, Cellphone, Email, Salary in cur.fetchall() :
            print("\nDNI:",DNI, "\nNombre Completo:",FullName,FullLastName, "\nPuesto:",Position,"\nEmail:",Email,"\n")
    #-------------------Consultar datos trabajadores por separado---------------#
    elif opciontrabajador == 2:
        print("Ver Datos de Trabajadores")
        inputOt2 = input("Escriba la cedula del trabajador: ")
        cur = db.cursor()
        cur.execute("SELECT * FROM trabajadores where DNI ='" +inputOt2+ "'")
        for row in cur.fetchall():
            print("\nCedula: ",row[0],"\nNombre Completo: ",row[1],row[2],"\nFecha de Nacimiento: ",row[3],"\nUbicacion: ",row[4],"\nFecha de Contratacion: ",row[5],"\nPuesto: ",row[6],"\nTelefono: ",row[7],"\nEmail: ",row[8],"\n")
    #-------------------Cambiar Correo de Trabajadores---------------#
    elif opciontrabajador == 3:
        print("Cambiar Correo de Usuarios")
        inputOt3 = input("Digite la Cedula del Trabajador ")
        cur = db.cursor()
        cur.execute("SELECT * FROM trabajadores where DNI ='" +inputOt3+ "'")
        for row in cur.fetchall():
            Op0 = row[0]
            Op1 = row[1]
            Op2 = row[2]
            Op3 = row[3]
            Op4 = row[4]
            Op5 = row[5]
            Op6 = row[6]
            Op7 = row[7]
            Op9 = row[9]
        newEmail = input("Digite el nuevo Email ")
        updated_email = """UPDATE trabajadores
                            SET FullName = %s,
                                FullLastName = %s,
                                Birthday = %s,
                                Location = %s,
                                DateOfHire = %s,
                                Position = %s,
                                Cellphone = %s,
                                Email = %s,
                                Salary = %s
                            WHERE DNI = %s;"""
        cur.execute(updated_email, (Op1, Op2, Op3, Op4, Op5, Op6, Op7,newEmail,Op9,Op0))
        db.commit()
        print("Email Cambiado con exito , el nuevo correo es: "+newEmail)
    #-------------------Enviar Correo a Trabajadores---------------#
    elif opciontrabajador == 4:
        print("Enviar Correo a Trabajador")
        inputOt4 = input("Digite la Cedula del Trabajador ")
        cur = db.cursor()
        cur.execute("SELECT * FROM trabajadores where DNI ='" +inputOt4+ "'")
        for row in cur.fetchall():
            Op8 = row[8]
        msjOT4 = input("Escriba el mensaje que va a enviar")
        remit = "soportprimeprogram@gmail.com"
        desto = Op8
        msj = msjOT4
        email = EmailMessage()
        email["From"] = remit
        email["To"] = desto
        email["Subject"] = "Correo de Recursos Humanos"
        email.set_content(msj)
        smtp = smtplib.SMTP_SSL("smtp.gmail.com")
        smtp.login(remit, "gbaabtuzmxgxrvhn")
        smtp.sendmail(remit, desto, email.as_string())
        smtp.quit()
        print("Correo Enviado")
    #-------------------Agregar Trabajadores---------------#
    elif opciontrabajador == 5:
        print("Agregar Trabajador")
    #-------------------Borrar Trabajadores---------------#
    elif opciontrabajador == 6:
        print("Eliminar Trabajador")

#-------------------Funcion login---------------#
def login():
    username = input("Digite el user ")
    password = input("Digite el pass: ")
    mydb = pymysql.connect(host="localhost",user="root",passwd="Halobat17.",database="rhdb")
    cursor = mydb.cursor()
    savequery = "SELECT * FROM users WHERE Usuario=%s AND Pass=%s" # Get the records with these username and password ONLY
    cursor.execute(savequery,(username,password))
    myresult = cursor.fetchall()
    if myresult: # If there is such a record, then success
        messagebox.showinfo("LOGIN",'LOGIN SUCCESSFUL')
        consultardatostrabajadores()
    else: # Wrong password
        messagebox.showerror("LOGIN ERROR","LOGIN ERROR")
        cursor.close()
        mydb.close()
        olvidopass()
login()
