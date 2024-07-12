from modregistro import *
from busqueda import buscarCiudad
import json
print("""
Bienvenido al registro de ciudades


Por favor ingrese una opcion
---------------------------------------------------
1 - Crear ciudad nueva
2 - Editar una ciudad existente
3 - Mostrar ciudades
4 - Buscar ciudad
0 - Salir
---------------------------------------------------
""")
opcion = input("Ingrese su opcion: ")
if opcion == '1':
    registrarCiudad()
elif opcion == '2':
    editarCiudades()
elif opcion == '3':
    leerCiudades()
elif opcion == '4':
    buscarCiudad()