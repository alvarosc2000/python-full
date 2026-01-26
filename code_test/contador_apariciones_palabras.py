def apariciones(cadena):
    dicc = {}


    for palabra in cadena:
        if palabra in dicc:
            dicc[palabra]  += 1
        else:
            dicc[palabra] = 1

    return dicc

print(apariciones([1,3,3,4,2]))