def ocurrencias(cadena):
    diccionario = {}
    
    for elem in cadena:
        if elem in diccionario:
            diccionario[elem] += 1
        else:
            diccionario[elem] = 1

    return diccionario

print(ocurrencias([1,3,4,2,4,5]))
