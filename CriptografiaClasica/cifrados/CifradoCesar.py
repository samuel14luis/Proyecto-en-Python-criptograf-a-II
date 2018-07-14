from utilidades.consola import *
class CifradoCesar():
    def menu(self,eleccion_salida):
        #Cifrar = 2  |  Descifrar = 3
        #Consola = 5 |  HTML = 7  | TXT = 11       
        print('mostrando menú de Cifrado César. Salida: '+str(eleccion_salida))
    
    def descripcion(self):
        mostrarMensaje('Descripción del Cifrado César')
        limpiarPantallaTecla('Presione una tecla para regresar> ')