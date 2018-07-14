from utilidades.consola import *
#Menu CC = Criptografía Clásica
def menuCifrados(cifrado,oconfig):
    cont = 0
    eleccion = 'seguir'
    output_config = oconfig #Configuración de salida consola:5, html:7, txt:11
    menu = [
        '[1] Configurar Salida',
        '-'*22,
        '[2] Cifrar',
        '[3] Descifrar',
        '[4] Breve descripción',
        '-'*22,
        '[0] volver'
    ]
    
    while eleccion == 'seguir':
        
        mostrarMenu(menu)

        op = input('Elija una opción> ')

        limpiarPantalla()

        if op == '1':
            #Configurar Salida
            output_config = configurarSalida(output_config)
            cont = 0
        elif op == '2':
            #Cifrar
            cifrado.menu(2*output_config)
            cont = 0
        elif op == '3':
            #Descifrar
            cifrado.menu(3*output_config)
            cont = 0
        elif op == '4':
            #Descripción
            cifrado.descripcion()
            cont = 0
        elif op == '0':
            #Salir
            return output_config
        else:
            cont += 1
            mostrarError('Debe ingresar una opción válida. {' + str(cont) + '}')
            eleccion = 'seguir'

    return output_config