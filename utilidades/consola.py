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