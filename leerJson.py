import json

def leerJson(nombre):
    file = open(nombre + ".json","r")
    datos = json.load(file)
    file.close()
    return(datos)

def guardarJson(nombre, datos):
    file = open(nombre + ".json","w")
    dump = json.dumps(datos,indent=4)
    file.write(dump)
    file.close()