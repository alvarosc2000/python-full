def secuencia_creciente(cadena):
    errores = 0

    for i in range(1, len(cadena)):
        if cadena[i] <= cadena[i-1]:
            errores += 1
            if errores >= 1:
                return False
            
            if i > 1 and cadena[i] <= cadena[i-2]:
                cadena[i] = cadena[i-1]
    return True

print(secuencia_creciente([1, 3, 2, 1]))
