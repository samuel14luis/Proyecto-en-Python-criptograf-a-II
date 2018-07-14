from utilidades.consola import getCodigo
from utilidades.generarArchivos.generarHTML import html_create
from utilidades.generarArchivos.generarTXT import txt_create
import webbrowser

class CifradoVigenere():
    def menu(self, eleccion_salida):  
        if eleccion_salida%2 == 0:
            texto_claro = input('Ingrese el texto en claro >_ ').lower().replace(' ','')
            palabra_clave = input('Ingrese la palabra clave >_ ').lower().replace(' ','')
            criptograma = self.cifrar(texto_claro,palabra_clave,eleccion_salida)
        else:
            criptograma = input('Ingrese el criptograma >_ ').lower().replace(' ','')
            palabra_clave = input('Ingrese la palabra clave >_ ').lower().replace(' ','')
            texto_claro = self.descifrar(criptograma,palabra_clave,eleccion_salida)

        print('')
    
    def cifrar(self,texto_claro,palabra_clave,eleccion_salida):
        criptograma = ''
        tabla = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
                c = (cod_m + cod_k)%len(tabla)
                    
            criptograma += tabla[c]
            j = (j+1)%len(palabra_clave)
        if eleccion_salida%5 == 0:
            print('Criptograma: ' + criptograma)
        if eleccion_salida%7 == 0:
            html_dir = input('Ingrese un nombre para el archivo HTML>')
            html_create(html_dir,'Cifrado Vigénere',criptograma,False)
        if eleccion_salida%11 == 0:
            txt_dir = input('Ingrese un nombre para el archivo TXT>')
            txt_create(txt_dir,criptograma,False)
        
        #Abrir Archivos
        if eleccion_salida%7 == 0:
            webbrowser.open_new_tab(html_dir+'.html')
        
        if eleccion_salida%11 == 0:
            webbrowser.open(txt_dir+'.txt')            
    
    def descifrar(self,texto_claro,palabra_clave,eleccion_salida):
        criptograma = ''
        tabla = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
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
                c = (cod_m - cod_k)%len(tabla)
                    
            criptograma += tabla[c]
            j = (j+1)%len(palabra_clave)
        if eleccion_salida%5 == 0:
            print('Texto en claro: ' + criptograma)
        if eleccion_salida%7 == 0:
            html_dir = input('Ingrese un nombre para el archivo HTML>')
            html_create(html_dir,'Cifrado Vigénere',criptograma,False)
        if eleccion_salida%11 == 0:
            txt_dir = input('Ingrese un nombre para el archivo TXT>')
            txt_create(txt_dir,criptograma,False)
        
        #Abrir Archivos
        if eleccion_salida%7 == 0:
            webbrowser.open_new_tab(html_dir+'.html')
        
        if eleccion_salida%11 == 0:
            webbrowser.open(txt_dir+'.txt')    

    def descripcion(self):
        mostrarMensaje('Descripción del Cifrado Vigenere')
        limpiarPantallaTecla('Presione una tecla para regresar> ')