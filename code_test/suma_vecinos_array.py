def suma_vecinos_array(cadena):
    lista = []

    for indice in range(len(cadena)):
        suma = 0
        if indice > 0:
            suma += cadena[indice-1]
        
        if indice < len(cadena)-1:
            suma += cadena[indice+1]
        
        suma += cadena[indice]
        lista.append(suma)

    return lista

print(suma_vecinos_array([4, 0, 1, -2, 3]))