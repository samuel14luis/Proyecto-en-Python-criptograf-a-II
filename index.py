import os
from utilidades.consola import limpiarPantalla, mostrarError, mostrarMenu
from CriptografiaModerna.menuCM import menuCM
from CriptografiaClasica.menuCC import menuCC

#DEFINICIÓN DE VARIABLES


#DEFINICIÓN DE FUNCIONES
def iniciarMenu():
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
        elif op == '2':
            eleccion = menuCM()
        elif op == '0':
            eleccion = 'salir'
        else:
            mostrarError('Debe ingresar una opción válida.')
            eleccion = 'seguir'


limpiarPantalla()
iniciarMenu()