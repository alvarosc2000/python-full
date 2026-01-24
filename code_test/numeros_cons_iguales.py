def numeros_consectuvos_iguales(cadena):
    for i in range(len(cadena)-1):
            if cadena[i] == cadena[i+1]:
                  return True
    return False

print(numeros_consectuvos_iguales([1, 2, 2, 3]))
print(numeros_consectuvos_iguales([1, 2, 3, 2]))