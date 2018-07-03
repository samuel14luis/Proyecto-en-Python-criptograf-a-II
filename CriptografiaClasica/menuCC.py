from utilidades.consola import limpiarPantalla

#Menu CC = Criptografía Clásica
def menuCC():
    eleccion = 'seguir'
    menu = [
        '[1] César',
        '[2] Atbash',
        '[3] Escritura Inversa',
        '[0] Salir'
    ]
    while eleccion == 'seguir':
        print ('Elija uno de los métodos de cifrado clásico')
        for i in range(len(menu)):
            print(menu[i])

        eleccion = input('Elija una opción> ')
        limpiarPantalla()
        if eleccion == '1':
            return menuCC()
        elif eleccion == '2':
            return menuCM()
        elif eleccion == '0':
            return 'salir'
        else:
            return eleccion

    return 'seguir'
