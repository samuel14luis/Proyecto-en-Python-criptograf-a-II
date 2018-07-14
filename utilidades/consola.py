import os

#comando para limpiar pantallas en windows
def limpiarPantalla():
    os.system('cls')

#comando para limpiar pantallas en windows al presionar una tecla
def limpiarPantallaTecla():
    input('Presione una tecla> ')
    os.system('cls')

def limpiarPantallaTecla(mensaje):
    input(mensaje)
    os.system('cls')

def outputMenu(output_config):
    menu = ['Seleccione como quiere que le mostremos los resultados:']
    if output_config%5 == 0:
        menu.append('[1] Consola (activado)')
    else:
        menu.append('[1] Consola ( )')

    if output_config%7 == 0:
        menu.append('[2] Archivo HTML (activado)')
    else:
        menu.append('[2] Archivo HTML ( )')

    if output_config%11 == 0:
        menu.append('[3] Archivo TXT (activado)')
    else:
        menu.append('[3] Archivo TXT ( )')
    menu.append('[0] Salir')

    return menu

def configurarSalida(output_config):
    #Configuración de salida consola:5, html:7, txt:11
    cont = 0
    eleccion = 'seguir'
    oconfig = output_config

    #Bucle del menú
    while eleccion == 'seguir':
        menu = outputMenu(oconfig)
        mostrarMenu(menu)

        op = input('Seleccione para activar/desactivar> ')

        limpiarPantalla()

        if op == '1':
            #Consola:5
            if oconfig%5 == 0:
                oconfig /= 5
            else:
                oconfig *= 5
            cont = 0
        elif op == '2':
            #HTML:7
            if oconfig%7 == 0:
                oconfig /= 7
            else:
                oconfig *= 7
            cont = 0
        elif op == '3':
            #TXT:11
            if oconfig%11 == 0:
                oconfig /= 11
            else:
                oconfig *= 11
            cont = 0
        elif op == '0':
            #Salir
            if oconfig == 1:
                mostrarError('Debe seleccionar como mínimo un modo de salida.')
            else:
                return oconfig
        else:
            cont += 1
            mostrarError('Debe ingresar una opción válida. {' + str(cont) + '}')
            eleccion = 'seguir'

#muestra el mensaje recibido como parámetro enmarcado en un cuadro con simbolos
def mostrarMensaje(mensaje):
    print('----' + '-'*len(mensaje))
    print('| ' + str(mensaje) + " |")
    print('----' + '-'*len(mensaje))

def mostrarError(error):
    mostrarMensaje(error)

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

def getCodigo(letra):
        cod = ord(letra)
        if cod >= 97 and cod <= 110:
            return cod - 97
        elif cod >= 111 and cod <= 122:
            return cod - 96
        elif cod == 241:
            return 14
        else:
            return -1