from leerJson import *

def buscarCiudad():
    ciudades = leerJson("ciudades")
    opcion = input("""Nombre | Pais | Codigo Postal
                   
Ingrese como desea buscar la ciudad: """)
    if opcion == "Nombre" or opcion == "Pais" or "Codigo Postal":    
        opcion2 = input("Ingrese el " + opcion.lower() + " de la ciudad: ")
        for ciudad in ciudades:
            if ciudad[opcion] == opcion2:
                print("Nombre: " + ciudad.get("Nombre"))
                print("Codigo Postal: " + ciudad.get("Codigo Postal"))
                print("Poblacion Estimada: " + ciudad.get("Poblacion Estimada"))
                print("Pais: " + ciudad.get("Pais"))