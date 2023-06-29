# Imported Libraries
import random
import string
import messagebox

# Variables for the creation of the random code
caracters = string.ascii_letters + string.digits
longitud = 6
secretcode = ''.join(random.choice(caracters)for _ in range(longitud))

# Variables for the connection with the email
Email_Master_User = "soportprimeprogram@gmail.com"
Email_Master_Password = "pxpigupgrvnshqre"

# Variables for the connection with the database
server = 'localhost'
database = 'Db_prueba_py'

# HTML and css format for sending the secret code email
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

#Create data the Users automatically
numero_aleatorio = random.randint(100, 999)
UserNameCreate = "Admin"+str(numero_aleatorio)

numero_aleatorio2 = random.randint(1000, 9999)
PasswordCreate = "RH"+str(numero_aleatorio2)
