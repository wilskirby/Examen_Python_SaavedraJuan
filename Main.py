import json
import register_user
import movistar


print (20 * ("-"))
print (10 * (""), ("Bienvenido a Movistar") ,10 * (""))
print (20 * ("-"))
print ("")
print ("Elije tu rol:")
print ("1. Usuario")
print ("2. Movistar")
print ("3. Salir del programa")

opc = input (":")
if opc == "1":
    register_user.menu_user()
    
elif opc == "2":
    movistar.menu_movistar()