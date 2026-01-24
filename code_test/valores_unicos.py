def valores_unicos(cadena):
    aux = []
    for i in range(len(cadena)):
        if cadena.count(cadena[i]) == 1:
            aux.append(cadena[i])
    
    return aux

print(valores_unicos([1,3,4,2,4,5,5,6,3,7,74,742]))