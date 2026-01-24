def valores_diferentes(cadena):
    for i in range(0, len(cadena)-1):
        for j in range(len(cadena)-1,-1,-1):
            if i != j and cadena[i] == cadena[j]:
                return False
    return True

print(valores_diferentes([1,2,3,4,5]))
