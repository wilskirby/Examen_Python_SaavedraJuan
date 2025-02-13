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

def aguser():
            for i in range(len(datos_user["Datos user"]["Nombre completo"])):
                
                nuevouser=input ("Nombre completo del Usuario: ")
                datos_user[i]["Datos user"]["Nombre completo"].append(nuevouser)
    


            guardardatosJSON()
aguser()







while True:
    def menu_user():
        print ("---Menu User---")
        print ("Que deseas hacer?")
        print ("1. Registrarse Usuario: ")
        print ("2. Iniciar sesion: ")
        print ("3. Cerrar programa")
    
        opt=input(":")
        opt=int(input(":"))

        if (opt == 1):
            aguser()

        elif (opt ==2):
            print ("")


