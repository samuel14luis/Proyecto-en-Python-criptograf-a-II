import webbrowser
def txt_create(_dir,_contenido,_abrir):
    f = open(_dir+'.txt','wb')
    f.write(_contenido.encode('utf-8'))
    f.close()
    if _abrir:
        webbrowser.open(_dir+'.txt')