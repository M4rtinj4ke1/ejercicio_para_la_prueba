import os, time
from funciones import *

while True:
    os.system('cls')
    print(' MENU CONTACTOS')
    print("""
    1. Agregar contactos
    2. Ver contacto
    3. Exportar archivo CSV
    4. Salir""")
    opc = int(input('Ingrese una opcion: '))
    if opc==1:
        opcion_1()
    elif opc==2:
        opcion_2()
    elif opc==3:
        opcion_3()
    else:
        opcion_4()
    time.sleep(2)