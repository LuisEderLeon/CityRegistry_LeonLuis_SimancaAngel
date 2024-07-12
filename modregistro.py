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
    input("""Ingrese 
          """)
    ciudades = leerJson("git/ciudades")
    for ciudad in ciudades:
        print(ciudad)

def editarciudades():
    codigo=input("Escriba el codigo postal de la ciudad para editar su informacion: ")
    
