def valores_diferentes(cadena):
    for i in range(len(cadena)-1):
        for j in range(len(cadena)-1,-1,-1):
            if cadena[i] == cadena[j] and i != j:
                return False
    return True

print(valores_diferentes([1, 2, 3, 4]))