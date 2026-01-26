def allLongestStrings(cadena):
    mayor = 0

    for elem in cadena:
        if len(elem) > mayor:
            mayor = len(elem)
    
    cadena_aux = []

    for elem in cadena:
        if len(elem) == mayor:
            cadena_aux.append(elem)
    
    return cadena_aux
    
print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))  # ["aba", "vcd", "aba"]
