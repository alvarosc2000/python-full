def suma_digitos(numero):
    suma = 0
    for x in str(numero):
        suma += int(x)
    return suma

print(suma_digitos(213))