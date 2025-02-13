import json
import users
import movistar


print (20 * ("-"))
print (10 * (""), ("Bienvenido a Movistar") ,10 * (""))
print (20 * ("-"))
print ("")
print ("Elije tu rol:")
print ("1. Usuario")
print ("2. Movistar")
print ("3. Salir del programa")
print (20 * ("-"))

opc = input (":")
if opc == "1":
    users.menu_user()
    
elif opc == "2":
    movistar.menu_movistar()

