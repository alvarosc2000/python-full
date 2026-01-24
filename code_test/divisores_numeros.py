def  divisores(numero):
    cadena = []
    for i in range(1,numero):
        if numero % i == 0:
            cadena.append(i)
    return cadena

print(divisores(8))