def maximo(lista):
    mayor = 0
    for i in range(len(lista)):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor

print(maximo([2,3,5,3,43,23,53,1,431,4,54,6,3]))