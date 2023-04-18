# Imported Libraries
import random
import string

# Variables for the creation of the random code
caracters = string.ascii_letters + string.digits
longitud = 6
secretcode = ''.join(random.choice(caracters)for _ in range(longitud))

# Variables for the connection with the email
Email_Master_User = "soportprimeprogram@gmail.com"
Email_Master_Password = "lgvozquxlykfijaq"

# Variables for the connection with the database
server = 'localhost'
database = 'Db_prueba_py'