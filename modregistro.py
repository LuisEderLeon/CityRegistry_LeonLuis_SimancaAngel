from leerJson import *

def registrarciudad():
    nombre = input("Escriba el nombre de la ciudad: ")
    postal=input("Escriba el codigo postal de la ciudad: ")
    poblacion=input("Escriba la poblacion estimada de la ciudad: ")
    pais=input("Escriba el pais al que pertenece la ciudad: ")
    
def leerCiudades():
    input("""Ingrese 
          """)
    ciudades = leerJson("ciudades")
    for ciudad in ciudades:
        print(ciudad)