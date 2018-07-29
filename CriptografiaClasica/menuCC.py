from utilidades.consola import *
from CriptografiaClasica.menuCifrados import *
from CriptografiaClasica.cifrados.CifradoCesar import CifradoCesar
#Menu CC = Criptografía Clásica
def menuCC(output_config):
    cont = 0
    eleccion = 'seguir'
    o_config = output_config

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
            #Cifrado César
            o_config = menuCifrados(CifradoCesar(), o_config)
            cont = 0
        elif op == '2':
            o_config = menuCifrados(CifradoCesar(), o_config)
            cont = 0
        elif op == '3':
            o_config = menuCifrados(CifradoCesar(), o_config)
            cont = 0
        elif op == '0':
            return ['seguir',o_config]
        else:
            cont += 1
            mostrarError('Debe ingresar una opción válida. {' + str(cont) + '}')
            eleccion = 'seguir'

    return ['seguir',o_config]
