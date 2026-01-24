def pares_mayores(lista, k):
    contador = 0
    for i in range(len(lista)):
        for j in range(i+1,len(lista)):
            if lista[i]+lista[j]>k:
                contador+=1
    return contador

# Pruebas
print(pares_mayores([1,2,3,4], 4))  # 3 → (2+3,2+4,3+4)
