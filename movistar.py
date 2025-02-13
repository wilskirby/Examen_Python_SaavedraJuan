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
    print (20 * ("-"))



menu_movistar()

def aguser():
            for i in range(len(datos_user["Datos user"]["Nombre completo"])):

                nuevouser=input ("Nombre completo del Usuario: ")
                datos_user[i]["Datos user"]["Nombre completo"].append(nuevouser)
             ## AÑadir algo al JSON pero algo estoy haciendo mal mhmmhmhmhmhmhmhm


            guardardatosJSON()