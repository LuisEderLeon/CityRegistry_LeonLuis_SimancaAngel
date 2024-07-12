from leerJson import *

def registrarciudad():
    nombre = input("Escriba el nombre de la ciudad: ")
    postal=input("Escriba el codigo postal de la ciudad: ")
    poblacion=input("Escriba la poblacion estimada de la ciudad: ")
    pais=input("Escriba el pais al que pertenece la ciudad: ")
    ciudades=leerJson("git/ciudades")
    ciudades.append({"Nombre": nombre, "Codigo Postal": postal, "Poblacion Estimada": poblacion, "Pais": pais})
    guardarJson("git/ciudades", ciudades)
    
def leerCiudades():
    opcion = input("""Ingrese que dato desea mostrar de las ciudades
          
Nombre | Postal | Poblacion | Pais
          
Ingrese su opcion: """)
    ciudades = leerJson("ciudades")
    for ciudad in ciudades:
        if opcion == "Nombre":
            print(ciudad["Nombre"])
        elif opcion == "Postal":
            print(ciudad["Codigo Postal"])
        elif opcion == "Poblacion":
            print(ciudad["Poblacion Estimada"])
        elif opcion == "Pais":
            print(ciudad["Pais"])
        
