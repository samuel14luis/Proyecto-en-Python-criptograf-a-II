#import os
import subprocess

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)

###########################################################################
seguir = 'cifrar'

print('--------------------BIENVENIDO AL CIFRADOR <Vigenere>--------------------')
print('')

while seguir == 'cifrar' or seguir == 'descifrar':
	print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
	print('')
	#LEER TEXTO EN CLARO
	if seguir == 'cifrar':
		texto_claro = input('Ingrese el texto en claro >_ ').lower()
	elif seguir == 'descifrar':
		texto_claro = input('Ingrese el criptograma >_ ').lower()
	print('')
	if seguir == 'cifrar':
		print('Texto en claro: ' + texto_claro)
	elif seguir == 'descifrar':
		print('Criptograma: ' + texto_claro)
	print('')
	criptograma = ''
	texto_claro = texto_claro.split(' ')
	for i in range(0, len(texto_claro), 1):		
		for j in range(1, len(texto_claro[i]) + 1, 1):
			criptograma += texto_claro[i][-j]
		criptograma += ' '
	if seguir == 'cifrar':
		print('Criptograma: ' + criptograma.strip())
	elif seguir == 'descifrar':
		print('Texto en claro: ' + criptograma.strip())
	print('')
	copy2clip(criptograma)
	print('>_ Se ha copiado al portapapeles')
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
