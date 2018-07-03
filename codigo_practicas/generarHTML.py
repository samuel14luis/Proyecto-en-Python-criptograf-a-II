def html_create(result):
    template = open("index.html","r")
    output = open("us.html","w")
    text = template.read().format(get_result = result)
    html = output.write(text)
    template.close()
    output.close()

html_create("hola mundo")