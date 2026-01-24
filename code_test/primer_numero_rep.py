def primer_numero(cadena):
    numero = -1
    cadena_a = []
    for i in range(0,len(cadena)):
        if cadena.count(cadena[i]) == 2 and numero == -1:
            numero = cadena[i]
    return numero

print(primer_numero([11, 1, 3, 5, 3, 2]))