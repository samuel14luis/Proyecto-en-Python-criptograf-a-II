import os
from utilidades.consola import *
from CriptografiaModerna.menuCM import menuCM
from CriptografiaClasica.menuCC import menuCC

#DEFINICIÓN DE VARIABLES


#DEFINICIÓN DE FUNCIONES
def iniciarMenu():
    mostrarError(' '*30 +'Bienvenido al programa'+' '*30)
    limpiarPantallaTecla('Presione una tecla para ingresar al menú de inicio>')

    cont = 0
    eleccion = 'seguir'
    output_config = 5
    menu = [
        '[1] Criptografía Clásica',
        '[2] Criptografía Moderna',
        '[3] Información del grupo',
        '[0] Salir'
    ]

    print ('Bienvenido')

    while eleccion == 'seguir':
        
        mostrarMenu(menu)

        op = input('Elija una opción> ')

        limpiarPantalla()

        if op == '1':
            aux = menuCC(output_config)
            eleccion = aux[0]
            output_config = aux[1]
            cont = 0
        elif op == '2':
            mostrarError('Aún no hay cifrados disponibles')
            limpiarPantallaTecla('Presione una tecla para regresar>')
            #aux = menuCM(output_config)
            #eleccion = aux[0]
            #output_config = aux[1]
            cont = 0
        elif op == '3':
            mostrarError('Información del grupo 2: Integrantes')
            print('LEÓN CRISPÍN, Maoe Jovaldo')
            print('LUIS MENDOZA, Samuel')
            print('MARÍN NUÑEZ, José Fernando')
            print('PANANA SOLÓRZANO, Flavio César')
            print('SÁNCHEZ ESCALANTE, Tony Abel')
            print(' ')
            limpiarPantallaTecla('Presione una tecla para regresar>')
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