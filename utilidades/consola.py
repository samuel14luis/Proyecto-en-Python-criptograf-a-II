import os

#comando para limpiar pantallas en windows
def limpiarPantalla():
    os.system('cls')

#muestra el mensaje recibido como parámetro enmarcado en un cuadro con simbolos
def mostrarError(mensaje):
    print('----' + '-'*len(mensaje))
    print('| ' + str(mensaje) + " |")
    print('----' + '-'*len(mensaje))

#Muestra un menu a partir de las opciones recibidas como parámetro
def mostrarMenu(opciones):
    for i in range(len(opciones)):
            print(opciones[i])

#Muestra un menu para salir o seguir en el menu
def salir():
    cont = 0
    menu = [
        'Seguro que desea salir del programa?',
        '[1] No, quiero quedarme un rato más.',
        '[0] Si, deseo salir ya del programa.'
    ]

    eleccion = 'x'

    while eleccion != '0' and eleccion != '1':
        
        mostrarMenu(menu)

        eleccion = input('> ')

        limpiarPantalla()

        if eleccion != '0' and eleccion != '1':
            cont += 1
            mostrarError('Debe ingresar una opción válida. {' + str(cont) + '}')

    if eleccion == '1':
        return 'seguir'
    else:
        return 'salir'

def despedida():
    limpiarPantalla()
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print('')
    print('>_ Desarrollado por Equipo N°2 ●•')
    print('')
    print('::::::::::  ::::::::   :::    ::: ::::::::::: :::::::::   ::::::::          ::::::::  ')
    print(':+:        :+:    :+:  :+:    :+:     :+:     :+:    :+: :+:    :+:        :+:    :+: ')
    print('+:+        +:+    +:+  +:+    +:+     +:+     +:+    +:+ +:+    +:+              +:+  ')
    print('+#++:++#   +#+    +:+  +#+    +:+     +#+     +#++:++#+  +#+    +:+            +#+    ')
    print('+#+        +#+  # +#+  +#+    +#+     +#+     +#+        +#+    +#+          +#+      ')
    print('#+#        #+#   +#+   #+#    #+#     #+#     #+#        #+#    #+#         #+#       ')
    print('##########  ###### ###  ########  ########### ###         ########         ########## ')
    print('')