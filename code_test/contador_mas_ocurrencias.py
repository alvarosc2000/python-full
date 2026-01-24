def mayor_ocurrencias(cadena):
    contador = 0
    numero = None

    for i in range(len(cadena)):
        if cadena.count(cadena[i]) > contador and numero != cadena[i]:
            contador = cadena.count(cadena[i])
            numero = cadena[i]
    
    return contador, numero

(c,n) = mayor_ocurrencias([1,2,3,2,3,2,5,5,3,1,3,2,3])
print(f"Las apariciones son {c} y del numero {n}")
        
