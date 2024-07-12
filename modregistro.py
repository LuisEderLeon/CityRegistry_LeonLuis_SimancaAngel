from leerJson import *

def registrarCiudad():
    nombre = input("Escriba el nombre de la ciudad: ")
    postal=input("Escriba el codigo postal de la ciudad: ")
    poblacion=input("Escriba la poblacion estimada de la ciudad: ")
    pais=input("Escriba el pais al que pertenece la ciudad: ")
    ciudades=leerJson("ciudades")
    ciudades.append({"Nombre": nombre, "Codigo Postal": postal, "Poblacion Estimada": poblacion, "Pais": pais})
    guardarJson("ciudades", ciudades)
    
def leerCiudades():
    ciudades = leerJson("ciudades")
    nombres = []
    postales = []
    poblaciones = []
    paises = []
    opcion = input("""Ingrese que dato desea mostrar de las ciudades
          
Nombre | Postal | Poblacion | Pais
          
Ingrese su opcion: """)
    for ciudad in ciudades:
        nombres.append(ciudad.get("Nombre"))
        postales.append(ciudad.get("Codigo Postal"))
        poblaciones.append(ciudad.get("Poblacion Estimada"))
        paises.append(ciudad.get("Pais"))
    nombres.sort()
    postales.sort()
    poblaciones.sort()
    paises.sort()
    if opcion == "Nombre":
        for nombre in nombres:
            print(nombre)
    elif opcion == "Postal":
        for postal in postales:
            print(postal)
    elif opcion == "Poblacion":
        for poblacion in poblaciones:
            print(poblacion)
    elif opcion == "Pais":
        for pais in paises:
            print(pais)
        
def editarCiudades():
    ciudades = list(leerJson("ciudades"))
    postal = input("Escriba el codigo postal de la ciudad a editar: ")
    for ciudad in ciudades:
        if ciudad["Codigo Postal"] == postal:
            opcion = input("""Nombre | Codigo Postal | Poblacion Estimada | Pais
                           
Ingrese que dato desea editar de la ciudad: """)
            if opcion == "Nombre" or opcion == "Codigo Postal" or opcion =="Poblacion Estimada" or opcion == "Pais":
                ciudad[opcion] = input("Ingrese el nuevo " + opcion.lower() + " de la ciudad: ")
            ciudades[ciudades.index(ciudad)] = ciudad
            guardarJson("ciudades", ciudades)