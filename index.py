import os
from utilidades.consola import *
from CriptografiaModerna.menuCM import menuCM
from CriptografiaClasica.menuCC import menuCC

#DEFINICIÓN DE VARIABLES


#DEFINICIÓN DE FUNCIONES
def iniciarMenu():
    cont = 0
    eleccion = 'seguir'
    menu = [
        '[1] Criptografía Clásica',
        '[2] Criptografía Moderna',
        '[0] Salir'
    ]

    print ('Bienvenido')

    while eleccion == 'seguir':
        
        mostrarMenu(menu)

        op = input('Elija una opción> ')

        limpiarPantalla()

        if op == '1':
            eleccion = menuCC()
            cont = 0
        elif op == '2':
            eleccion = menuCM()
            cont = 0
        elif op == '0':
            eleccion = salir()
        else:
            cont += 1
            mostrarError('Debe ingresar una opción válida. {' + str(cont) + '}')
            eleccion = 'seguir'


limpiarPantalla()
iniciarMenu()
despedida()
input('')
limpiarPantalla()