import json

def abrirplanesJSON():
    dicFinal = {}
    with open(f"./planes.json", 'r') as newFile:
        dicFinal = json.load(newFile)
    return dicFinal

def guardarplanesJSON(dic):
    with open("./planes_userjson", 'w') as outFile:
        json.dump(dic, outFile, indent=4, ensure_ascii=True)

planes_user=abrirplanesJSON()

def ver_planes():
    for i in range(len(planes_user["Planes"]["Servicio"])):
        print(planes_user["Planes"]["Servicio"][i])
        print (20 * ("-"))

def menu_user():
    print ("---Menu User---")
    print ("Hola User, que deseas hacer?")
    print ("1. Ver planes")
    print ("2. Cerrar programa")

    while True:
        opt=input(":")

        if (opt == "1"):
            print (20 * ("-"))
            ver_planes ()

        elif (opt == "2"):
            break
