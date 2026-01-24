def numerosconsecut(cadena):
    for i in range(len(cadena)-1):
        if cadena[i] == cadena[i+1]:
            return True
    return False

print(numerosconsecut([1,2,3,4]))