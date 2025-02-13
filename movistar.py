import json

def abrirdatosJSON():
    dicFinal = {}
    with open(f"./datos_user.json", 'r') as newFile:
        dicFinal = json.load(newFile)
    return dicFinal

def guardardatosJSON(dic):
    with open("./datos_userjson", 'w') as outFile:
        json.dump(dic, outFile, indent=4, ensure_ascii=True)

datos_user=abrirdatosJSON()

def menu_movistar():
    print (20 * ("-"))
    print ("\nBienvenido Movistar")
    print ("Que deseas realizar?")
    print("1. Agregar un usuario")
    print ("2. Ver todos los usuarios")
    print (20 * ("-"))
    while True:
        opt=input(":")

        if (opt == "1"):
            print (20 * ("-"))
            aguser ()

        elif (opt == "2"):
            ver_users()




def aguser():
            for i in range(len(datos_user["Datos user"]["Nombre completo"])):

                nuevouser=input ("Nombre completo del Usuario: ")
                datos_user["Datos user"]["Nombre completo"][i].append(nuevouser)
             ## AÑadir algo al JSON pero algo estoy haciendo mal mhmmhmhmhmhmhmhm


            guardardatosJSON()

def ver_users():
        for i in range(len(datos_user["Datos user"])):
            print (datos_user["Datos user"]["Nombre completo"])
            print (datos_user["Datos user"]["Direccion"])   
            print (datos_user["Datos user"]["Contacto"])
            print (datos_user["Datos user"]["Años"])
            print (datos_user["Datos user"]["Servicio"])
