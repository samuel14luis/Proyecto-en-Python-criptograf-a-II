#!/usr/bin/env python
# -*- coding: utf-8 -*-
from io import open
from generarHTML import html_create
html_create("index","_cifrado","_contenido","_nombre", True)

#archivo_texto = open('prueba.html', 'w') 
# w -> write | Modo Escritura   write(contenido)
# r -> read  | Modo Lectura     read(), readlines() devuelve una lista
# a -> append| Modo Añadir

#contenido = "Hola, Mundo!\nLinea 2\nLinea 3\nLinea 4\nLinea 5\nLinea 6\najáñn"

#archivo_texto.write(contenido.decode('utf-8'))


#LEYENDO ARCHIVOS
#archivo_texto = open('prueba.html', 'r') 
#lineas = archivo_texto.readlines()
#print(lineas[0])
#FIN LEYENDO ARCHIVOS

#MODIFICANDO ARCHIVO
#archivo_texto = open('prueba.html', 'a') 
#archivo_texto.write('\nlínea añadida')
#FIN MODIFICANDO ARCHIVO

#archivo_texto.close()

#print(contenido.decode('ascii','ignore')) #para ignorar los carácteres especiales como tildes y ñ

#print(u'xd ñ ajá ajé ají ajó ajú') #practicas con codificacion unicode
