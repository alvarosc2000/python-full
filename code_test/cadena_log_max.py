def cadenaLongMax(cadena):
    if cadena == []:
        return []
    
    maximo = 0
    for elem in cadena:
        if len(elem) > maximo:
            maximo = len(elem)
    
    cadena_aux = []
    for elem in cadena:
        if len(elem) == maximo:
            cadena_aux.append(elem)
    

    return cadena_aux

print(cadenaLongMax(["aba", "aa", "ad", "vcd", "aba"]))
print(cadenaLongMax(["a"]))
print(cadenaLongMax([]))
