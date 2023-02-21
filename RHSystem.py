import random
import pymysql
from email.message import EmailMessage
import smtplib
import messagebox
#-------------------Funcion Inicio---------------#
def prmenust():
    prmst = int(input("{-----------------RH SYSTEM-----------------}\n!WELCOME!\n1.Login\n2.Register\n3.Cerrar\n"))
    if prmst == 1:
        login()
    elif prmst == 2:
        print("Register")
        registeruser()
    elif prmst == 3:
        print("GOODBYE")
    else:
        print("Digite una opcion correcta")
        prmenust()
      
#-------------------Funcion login---------------#
def login():
    username = input("Digite el user ")
    password = input("Digite el pass: ")
    mydb = pymysql.connect(host="localhost",user="root",passwd="Halobat17.",database="rhdb")
    cursor = mydb.cursor()
    savequery = "SELECT * FROM users WHERE Usuario=%s AND Pass=%s" # Get the records with these username and password ONLY
    cursor.execute(savequery,(username,password))
    myresult = cursor.fetchall()
    if myresult:
        messagebox.showinfo("LOGIN Corecto",'Bienvenid@'+username)
        consultardatostrabajadores()
    else: 
        messagebox.showerror("LOGIN Fallido","Usuario o Pass no encontrados")
        cursor.close()
        mydb.close()
        cerrarinput = input("Desea cerrar recuperar el password?\nS=Si\nN=No\n")
        if cerrarinput.upper() == "S":
            olvidopass()
        elif cerrarinput.upper() == "N":
            print("Cerrando programa\nNos vemos",username)
              
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
        oprec = input("Volver a intentarlo?\nS=Si\nN=No\n")
        if oprec.upper == "S":
            olvidopass()
        else:
            login()

#--------------------Funcion Registrarse-------------------#
def registeruser():
    print("Registrar un Administrador Nuevo")
    db = pymysql.connect(host="localhost",user="root",passwd="Halobat17.",database="rhdb")
    curs = db.cursor()
    insert_stmt = (
    "INSERT INTO users(Usuario, Email, SecurityQuestion, Pass)"
    "VALUES (%s, %s, %s, %s)"
    )
    in0 = input("Digite el Usuario: ")
    in1 = input("Digite el Email: ")
    in2 = input("Digite la respuesta a su SQ: ")
    in3 = input("Digte la Password: ")
    data = (in0, in1, in2, in3)
    try:
        curs.execute(insert_stmt, data)
        db.commit()
        messagebox.showinfo("Register","Usuario Registrado")
        prmenust
    except:
        db.rollback()
        messagebox.showerror("Register","Usuario no Registrado")
        prmenust()
          
#-------------------Consulta Trabajadores---------------#
def consultardatostrabajadores():
    print("Sistema Recursos Humanos\n")
    db = pymysql.connect(
        host="localhost",
        user="root",
        passwd="Halobat17.",
        db="rhdb"
    )
    opciontrabajador = int(input("{----------Menu----------}\n1.Trabajadores Disponibles\n2.Ver Datos de Trabajadores\n3.Cambiar Correo de Usuarios\n4.Enviar Correo a Trabajador\n5.Agregar Trabajador Trabajador\n6.Eiminar Trabajador\n7.Salir\n"))
    #-------------------Cosnultar la Lista de trabajadores general---------------#
    if opciontrabajador == 1:
        print("Trabajadores Disponibles")
        cur = db.cursor()
        cur.execute("SELECT * FROM trabajadores")
        for DNI, FullName, FullLastName, Birthday, Location, DateOfHire, Position, Cellphone, Email, Salary in cur.fetchall() :
            print("\nDNI:",DNI, "\nNombre Completo:",FullName,FullLastName, "\nPuesto:",Position,"\nEmail:",Email,"\n")
        consultardatostrabajadores()
    #-------------------Consultar datos trabajadores por separado---------------#
    elif opciontrabajador == 2:
        print("Ver Datos de Trabajadores")
        inputOt2 = input("Escriba la cedula del trabajador: ")
        cur = db.cursor()
        cur.execute("SELECT * FROM trabajadores where DNI ='" +inputOt2+ "'")
        for row in cur.fetchall():
            print("\nCedula: ",row[0],"\nNombre Completo: ",row[1],row[2],"\nFecha de Nacimiento: ",row[3],"\nUbicacion: ",row[4],"\nFecha de Contratacion: ",row[5],"\nPuesto: ",row[6],"\nTelefono: ",row[7],"\nEmail: ",row[8],"\n")
            consultardatostrabajadores()
    #-------------------Cambiar Datos de Trabajadores---------------#
    elif opciontrabajador == 3:
        print("Cambiar Datos de Trabajadores")
        inputOt3 = input("Digite la Cedula del Trabajador ")
        cur = db.cursor()
        cur.execute("SELECT * FROM trabajadores where DNI ='" +inputOt3+ "'")
        for row in cur.fetchall():
            Op0 = row[0]
            Op1 = row[1]
            Op2 = row[2]
            Op3 = row[3]
            Op5 = row[5]
            Op9 = row[9]
        newlocation = input("Digite la nueva Ubicacion ")
        newposition = input("Digite el nuevo titulo ")
        newcelllphone = input("Digite el nuevo Telefono ")
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
        cur.execute(updated_email, (Op1, Op2, Op3, newlocation, Op5, newposition, newcelllphone, newEmail,Op9,Op0))
        db.commit()
        messagebox.showinfo("Actualizacion de datos","Los datos fueron actualizados con exito")
        consultardatostrabajadores()
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
        print("Correo Enviado con Exito")
        consultardatostrabajadores()
    #-------------------Agregar Trabajadores---------------#
    elif opciontrabajador == 5:
        print("Agregar Trabajador")
        curs = db.cursor()
        insert_stmt = (
        "INSERT INTO trabajadores(DNI, FullName, FullLastName, Birthday, Location, DateOfHire, Position, Cellphone, Email, Salary)"
        "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        in0 = int(input("Digite la Cedula: "))
        in1 = input("Digite el Nombre Completo: ")
        in2 = input("Digite los Apellidos Completos: ")
        in3 = input("Digte la Fecha de Nacimento con el Formato 0/0/0: ")
        in4 = input("Digite la Ubicacion: ")
        in5 = input("Digite la Fecha de contratacion con el Formato 0/0/0: ")
        in6 = input("Digite el Titulo: ")
        in7 = input("Digite el Telefono")
        in8 = input("Digite el Correo")
        data = (in0, in1, in2, in3, in4, in5, in6, in7, in8, 0)
        try:
            curs.execute(insert_stmt, data)
            db.commit()
            consultardatostrabajadores()
        except:
            db.rollback()          
    #-------------------Borrar Trabajadores---------------#
    elif opciontrabajador == 6:
        print("Eliminar Trabajador")
        cursor = db.cursor()
        sql_Delete_query = """Delete from trabajadores where DNI = %s"""
        # row to delete
        DNIinput = input("Digite la cedula del trabajador: ")
        cursor.execute(sql_Delete_query, (DNIinput,))
        db.commit()
        print("Record Deleted successfully ")
        if db:
            messagebox.showinfo("Accept",'Se elimino a '+DNIinput)
            consultardatostrabajadores()
        else:
            messagebox.showinfo("Deny",'No se encontro a '+DNIinput)
            consultardatostrabajadores()
    elif opciontrabajador == 7:
        print("Devolviendose: ")
        prmenust()
    else:
        print("Opcion Incorrecta\nIntente denuevo")
        opciontrabajador()
                
#-------------------Llamar Funcion Principal---------------#
prmenust()

"""(Sistema de Salarios (Planeando Agregarlo))
    Bach = 280000
    Lic = 360000
    Mast = 450000
    Doc = 510000

    Levbel = input("Digite el nivel: ")
    if Levbel == "Bach":
        Falinput = int(input("Digite las faltas: "))
        calc = 18600 * Falinput
        Resf = Bach - calc
        print("Su pago es: ",Resf)
    elif Levbel == "Lic":
        Falinput = int(input("Digite las faltas: "))
        calc = 24000 * Falinput
        Resf = Lic - calc
        print("Su pago es: ",Resf)
    elif Levbel == "Mast":
        Falinput = int(input("Digite las faltas: "))
        calc = 30000 * Falinput
        Resf = Mast - calc
        print("Su pago es: ",Resf)
    elif Levbel == "Doc":
        Falinput = int(input("Digite las faltas: "))
        calc = 34000 * Falinput
        Resf = Mast - calc
        print("Su pago es: ",Resf)
"""
