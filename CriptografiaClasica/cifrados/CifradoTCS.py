from math import ceil

def selectionSort2(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax = 0
		for location in range(1, fillslot+1):
			if alist[location][0] > alist[positionOfMax][0]:
				positionOfMax = location
		temp = alist[fillslot][0]
		alist[fillslot][0] = alist[positionOfMax][0]
		alist[positionOfMax][0] = temp

def selectionSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax = 0
		for location in range(1, fillslot+1):
			if alist[location][0] > alist[positionOfMax][0]:
				positionOfMax = location
		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp

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

#Código de TCS

eleccion = 'cifrar'
while eleccion == 'cifrar' or eleccion == 'descifrar':    
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print('')    
    #PEDIR DATOS
    if eleccion == 'cifrar':
        texto_claro = input('Ingrese el texto en claro >_ ').lower().replace(' ','')
    elif eleccion == 'descifrar':
        #Pedir Criptograma
        texto_claro = input('Ingrese el criptograma >_ ').lower().replace(' ','')
    #Pedir Palabra Clave
    palabra_clave = input('Ingrese la palabra clave >_ ').lower().replace(' ','')
    print('')

    #MOSTRAR DATOS RECIBIDOS EN PANTALLA    
    if eleccion == 'cifrar':
        print('Texto en claro: ' + texto_claro)
    elif eleccion == 'descifrar':
        print('Criptograma: ' + texto_claro)
    print('')

    #PROCESAR DATOS
    
    filas = ceil(len(texto_claro)/len(palabra_clave))
    columnas = len(palabra_clave)
    matriz = []

    #Generar matriz con los id puestos y cadena de texto vacía   
    for i in range(0,columnas,1):
        matriz.append([getCodigo(palabra_clave[i]),''])
    
    #Agregar el texto a la matriz
    cont = 0
    for i in range(0, filas*columnas):
        if(i < len(texto_claro)):
            matriz[cont][1] += texto_claro[i]
        else:
            matriz[cont][1] += '$'
        cont= (cont+1)%columnas
    
    #Ordenar la matriz de acuerdo al id de la letra de la palabra clave
    selectionSort(matriz)
    
    #Agregar el texto ya cifrado/descifrado al criptograma, listo para mostrar
    criptograma = ''
    for i in range(0,columnas):
        criptograma += matriz[i][1]
        print(criptograma)
    

    #MOSTRAR RESULTADOS
    if eleccion == 'cifrar':
        print('Criptograma: ' + criptograma)
    elif eleccion == 'descifrar':
        print('Texto en claro: ' + criptograma)       

    eleccion = input('Elija una opción CIFRAR\DESCIFRAR\SALIR >_ ').lower()

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