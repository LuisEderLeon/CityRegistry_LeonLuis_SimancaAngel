from modregistro import *
import json
print("""
Bienvenido al registro de ciudades


Por favor ingrese una opcion
---------------------------------------------------
1 - Crear ciudad nueva
2 - Editar una ciudad existente
3 - Mostrar ciudades
0 - Salir
---------------------------------------------------
""")
opcion = input("Ingrese su opcion: ")
if opcion == '1':
    registrarciudad()
elif opcion == '2':
    editarciudades()
elif opcion == '3':
    leerCiudades()