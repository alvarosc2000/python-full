def primer_caracter(cadena):
    cadena_aux = cadena.split()
    contador = 0
    valor = ""
    for i in range(len(cadena)-1):
        if valor == "" and cadena.count(cadena[i]) == 1:
            valor += cadena[i]
    
    return valor

print(primer_caracter("Hola mundo esto es una prueba y hay Hen total 12 palabras"))