import os
tabla = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
seguir = 'cifrar'

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

print('--------------------BIENVENIDO AL CIFRADOR <Vigenere>--------------------')
print('')
while seguir == 'cifrar' or seguir == 'descifrar':
	print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
	print('')
	if seguir == 'cifrar':
		texto_claro = input('Ingrese el texto en claro >_ ').lower().replace(' ','')
	elif seguir == 'descifrar':
		texto_claro = input('Ingrese el criptograma >_ ').lower().replace(' ','')
	palabra_clave = input('Ingrese la palabra clave >_ ').lower().replace(' ','')
	criptograma = ''
	print('')
	if seguir == 'cifrar':
		print('Texto en claro: ' + texto_claro)
	elif seguir == 'descifrar':
		print('Criptograma: ' + texto_claro)
	print('')
	j = 0
	for i in range(len(texto_claro)):		
		m = texto_claro[i]
		k = palabra_clave[j]
		#obtenemos los codigos de m y k
		cod_m = getCodigo(m)
		cod_k = getCodigo(k)
		if cod_m == -1:
			continue
		elif cod_k == -1:
			j = (j+1)%len(palabra_clave)
			continue
		else:
			if seguir == 'cifrar':
				c = (cod_m + cod_k)%len(tabla)
			elif seguir == 'descifrar':
				c = (cod_m - cod_k)%len(tabla)
			
		criptograma += tabla[c]
		j = (j+1)%len(palabra_clave)
	if seguir == 'cifrar':
                print('Criptograma: ' + criptograma)
	elif seguir == 'descifrar':
                print('Texto en Claro: ' + criptograma)
	
	print('')
	seguir = input('Elija una opción CIFRAR\DESCIFRAR\SALIR >_ ').lower()
	print('')
	#os.system('cls')
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
