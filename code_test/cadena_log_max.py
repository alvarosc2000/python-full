def cadenaLongMax(cadena):
    if cadena == []:
        return []
    
    lista = []
    maxima_log = 0

    for elem in cadena:
        if len(elem) > maxima_log:
            maxima_log = len(elem)
    
    for elem2 in cadena:
        if len(elem2) == maxima_log:
            lista.append(elem2)
    
    return lista

print(cadenaLongMax(["aba", "aa", "ad", "vcd", "aba"]))
print(cadenaLongMax(["a"]))
print(cadenaLongMax([]))
