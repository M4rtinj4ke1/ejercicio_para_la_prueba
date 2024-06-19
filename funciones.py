contactos = []
def opcion_1():
    print('Agregar contacto')
    nombre = validar_nombre()
    telefono = validar_telefono()
    correo = validar_correo()
    contacto = {'nombre':nombre, 'telefono':telefono, 'correo':correo}
    contactos.append(contacto)
    print('Contacto agregado')

def opcion_2():
    if not contactos:
        print('No exiten contactos, vuelva a la opcion 1')
    else:
        print('\tLista de contactos')
        for c in contactos:
            print("NOMBRE:",c['nombre'])
            print("TELEFONO:",c['telefono'])
            print("CORREO:",c['correo'],'\n')
def opcion_3():
    if not contactos:
        print('No exiten contactos, vuelva a la opcion 1')
    else:
        nombre_archivo = input('Ingrese nombre del archivo: ')+".csv"
        import csv
        with open (nombre_archivo,'w',newline='') as archivo:
            escritor = csv.DictWriter(archivo, contactos[0].keys())
            escritor.writerows(contactos)

def opcion_4():
    print("GRACIA, ADIOS")
    exit()    

def validar_nombre():
    nom = input('Ingrese nombre: ')
    if len(nom.strip())>=3 and nom.isalpha():
        return nom
    else:
        print('ERROR! el nombre debe tener al menos 3 caracteres y solo letras!')
 
def validar_telefono():
    while True:
        try:
            tel = int(input('Ingrese numero de telefono: '))
            if len(str(tel))==9 and str(tel)[0]==9:
                return tel
            else:
                print('ERROR! el telefono debe comenzar con 9 y tener 9 digitos')
        except:
            print ('ERROR! debe ingresar un numero entero')

def validar_correo():
    while True:
        cor = input('Ingrese correo: ')
        if cor.strip().lower().endswith('@gmail.com') and len(cor.strip())>=13:
            return cor
        else:
            print('ERROR! correo incorrecto')