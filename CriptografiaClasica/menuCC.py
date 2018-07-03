from utilidades.consola import *
from CriptografiaClasica.menuCifrados import *
#Menu CC = Criptografía Clásica
def menuCC():
    cont = 0
    eleccion = 'seguir'
    menu = [
        '[1] César',
        '[2] Atbash',
        '[3] Escritura Inversa',
        '[0] volver'
    ]
    
    while eleccion == 'seguir':
        
        mostrarMenu(menu)

        op = input('Elija una opción> ')

        limpiarPantalla()

        if op == '1':
            menuCifrados()
            cont = 0
        elif op == '2':
            menuCifrados()
            cont = 0
        elif op == '3':
            menuCifrados()
            cont = 0
        elif op == '0':
            return 'seguir'
        else:
            cont += 1
            mostrarError('Debe ingresar una opción válida. {' + str(cont) + '}')
            eleccion = 'seguir'

    return 'seguir'
