from utilidades.consola import getCodigo
from utilidades.generarArchivos.generarHTML import html_create
from utilidades.generarArchivos.generarTXT import txt_create
import webbrowser

class CifradoAtbash():
    def menu(self, eleccion_salida):  
        if eleccion_salida%2 == 0:
            texto_claro = input('Ingrese el texto en claro >_ ').lower().replace(' ','')
            criptograma = self.cifrar(texto_claro,eleccion_salida)
        else:
            criptograma = input('Ingrese el criptograma >_ ').lower().replace(' ','')
            texto_claro = self.descifrar(criptograma,eleccion_salida)

        print('')
    
    def cifrar(self,texto_claro,eleccion_salida):
        criptograma = ''
        tabla = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
        if eleccion_salida%5 == 0:
            print('Criptograma: ' + criptograma)
        if eleccion_salida%7 == 0:
            html_dir = input('Ingrese un nombre para el archivo HTML>')
            html_create(html_dir,'Cifrado Atbash',criptograma,False)
        if eleccion_salida%11 == 0:
            txt_dir = input('Ingrese un nombre para el archivo TXT>')
            txt_create(txt_dir,criptograma,False)
        
        #Abrir Archivos
        if eleccion_salida%7 == 0:
            webbrowser.open_new_tab(html_dir+'.html')
        
        if eleccion_salida%11 == 0:
            webbrowser.open(txt_dir+'.txt')            
    
    def descifrar(self,texto_claro,eleccion_salida):
        criptograma = ''
        tabla = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
        if eleccion_salida%5 == 0:
            print('Texto en claro: ' + criptograma)
        if eleccion_salida%7 == 0:
            html_dir = input('Ingrese un nombre para el archivo HTML>')
            html_create(html_dir,'Cifrado Atbash',criptograma,False)
        if eleccion_salida%11 == 0:
            txt_dir = input('Ingrese un nombre para el archivo TXT>')
            txt_create(txt_dir,criptograma,False)
        
        #Abrir Archivos
        if eleccion_salida%7 == 0:
            webbrowser.open_new_tab(html_dir+'.html')
        
        if eleccion_salida%11 == 0:
            webbrowser.open(txt_dir+'.txt')    

    def descripcion(self):
        mostrarMensaje('Descripción del Cifrado Atbash')
        limpiarPantallaTecla('Presione una tecla para regresar> ')