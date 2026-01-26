def maximo(lista):
    mayor = 0
    frec_mayor = 0
    for elem in range(len(lista)):
        if lista.count(lista[elem]) > frec_mayor and lista[elem] != mayor:
            mayor = lista[elem]
            frec_mayor = lista.count(lista[elem])
    
    return mayor

print(maximo([2,3,5,3,43,23,53,1,431,4,54,6,3]))