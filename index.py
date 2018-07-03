import os

#DEFINICIÓN DE VARIABLES
eleccion = 'seguir'
menu = [
    '[1] Criptografía Clásica',
    '[2] Criptografía Moderna',
    '[0] Salir'
]

#DEFINICIÓN DE FUNCIONES
def limpiarPantalla():
    os.system('cls')

def iniciarMenu():
    while eleccion == 'seguir':
        print ('Bienvenido')
        for i in range(len(menu)):
            print(menu[i])

        eleccion = input('Elija una opción> ')
        limpiarPantalla()
        eleccion = evaluarEleccion(eleccion)

def evaluarEleccion(eleccion):
    if eleccion == '1':
        return criptografiaClasica()
    elif eleccion == '2':
        return criptografiaModerna()
    else:
        return eleccion

def criptografiaClasica():
    print('iniciando criptografía Clásica')
    return 'seguir'

def criptografiaModerna():
    print('iniciando criptografía Moderna')
    return 'seguir'


limpiarPantalla()
iniciarMenu()