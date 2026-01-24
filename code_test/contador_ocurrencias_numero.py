def ocurrencias_numero(cadena, valor):
    contador = 0
    for elem in cadena:
        if elem == valor:
            contador+=1
    return contador

print(ocurrencias_numero([1,2,3,2,3,4,5,2,4],2))