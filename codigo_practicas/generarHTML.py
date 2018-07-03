import webbrowser
def html_create(_dir,_cifrado,_contenido,_nombre):
    f = open(_dir+'.html','wb')

    mensaje = """<!DOCTYPE html>
    <html lang="en">

    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>"""+_cifrado+""" - Resultados para @"""+_nombre+"""</title>
        <style>
            body {
                background: white;
                color: rgb(104, 104, 104);
            }

            .contenido {
                background: rgb(255, 254, 254);
                width: 70%;
                border-radius: 2px;
                box-shadow: 2px 2px 10px gray;
                min-height: 85vh;
                position: absolute;
                left: 50%;
                top: 50px;
                bottom: 50px;
                transform: translateX(-50%);
            }

            .texto {
                background: rgb(255, 255, 255);    
                max-height: 70%;
                min-height: 70%;
                text-overflow: ellipsis;
                overflow: auto;
            }

            .texto::-webkit-scrollbar {
                width: 10px;
                background: white;
            }

            .texto::-webkit-scrollbar-thumb {
                width: 10px;
                background: orange;
                border-radius: 5px;
            }

            .titulo {
                text-align: center;
            }

            .pie {
                text-align: right;
                right: 20px;
                position: absolute;
                bottom: 0px;
            }

            .resultado {
                margin: 20px 100px;
                text-align: justify;
            }
        </style>
    </head>

    <body>
        <div class="contenido">
            <h1 class="titulo">"""+_cifrado+"""</h1>
            <div class="texto">
                <p class="resultado">
                    """+_contenido+"""
                </p>
            </div>
            <h4 class="pie">Resultados para @"""+_nombre+"""</h4>

        </div>
    </body>

    </html>"""

    f.write(mensaje.encode('utf-8'))
    f.close()
    webbrowser.open_new_tab(_dir+'.html')