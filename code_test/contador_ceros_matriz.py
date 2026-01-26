def contador_ceros(matriz):
    contador = 0

    for fila in range(len(matriz)):
        for colum in range(len(matriz[0])):
            if matriz[fila][colum] == 0:
                contador += 1
    return contador

print(contador_ceros([[0,1,0],[2,0,4]]))