def indices_el(cadena, valor):
    # Recorremos hacia adelante para primer índice
    indice1 = -1
    for i in range(len(cadena)):
        if cadena[i] == valor:
            indice1 = i
            break

    # Recorremos hacia atrás para último índice
    indice2 = -1
    for j in range(len(cadena)-1, -1, -1):
        if cadena[j] == valor:
            indice2 = j
            break

    return indice1, indice2

# --- Pruebas ---
print(indices_el([1,2,3,2,4,2], 2))  # (1,5)
print(indices_el([1,2,3], 5))        # (-1,-1)
print(indices_el([7,8,7,9,7], 7))    # (0,4)
