def invertir_lista(cadena):
    lista = []

    for i in range(len(cadena)-1,-1,-1):
        lista.append(cadena[i])
    return lista

print(invertir_lista(["a", "b", "c"]))