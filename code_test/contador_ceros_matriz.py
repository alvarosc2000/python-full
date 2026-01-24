def contador_ceros(matriz):
    contador = 0
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == 0:
                contador += 1
    return contador

print(contador_ceros([[0,1,0],[2,3,4]]))