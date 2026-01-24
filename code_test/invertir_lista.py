def invertir_lista(cadena):
    aux = []
    
    for elem in range(len(cadena)-1,-1,-1):
        aux.append(cadena[elem])
    
    return aux


print(invertir_lista(["a", "b", "c"]))