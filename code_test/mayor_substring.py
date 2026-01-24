def allLongestStrings(cadena):
    mayor_long = 0
    for elem in cadena:
        if len(elem) > mayor_long:
            mayor_long = len(elem)
    
    aux = []

    for e in cadena:
        if len(e) == mayor_long:
            aux.append(e)
    return aux
    
print(allLongestStrings(["aba", "aa", "ad", "vcd", "aba"]))  # ["aba", "vcd", "aba"]
