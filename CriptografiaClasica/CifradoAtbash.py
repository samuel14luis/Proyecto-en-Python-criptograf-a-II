from utilidades.consola import *
import os
tabla = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
seguir = 'si'
print('--------------------BIENVENIDO AL CIFRADOR <Atbash>--------------------')
print('')
while seguir == 'si':
	print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
	print('')
	texto_claro = input('Ingrese el texto en claro >_ ').lower().replace(' ','')
	criptograma = ''
	print('')
	print('Texto en claro: ' + texto_claro)
	print('')
	for i in range(len(texto_claro)):
		cod = ord(texto_claro[i])
		#print(cod)
		if cod >= 97 and cod <= 110:
			cod = cod - 96
		elif cod >= 111 and cod <= 122:
			cod = cod - 95
		elif cod == 241:
			cod = 15
		else:
			continue
		criptograma += tabla[-cod]
	print('Criptograma: ' + criptograma)
	print('')
	seguir = input('Desea continuar? SI/NO >_ ').lower()
	print('')