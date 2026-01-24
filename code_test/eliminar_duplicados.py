def eliminarDuplicados(cadena):
    cadena_aux = ""
    for x in range(len(cadena)):
        if cadena[x] not in cadena_aux:
            cadena_aux += cadena[x]
    return cadena_aux

print(eliminarDuplicados("programming"))