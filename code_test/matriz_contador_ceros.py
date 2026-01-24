def contador_de_ceros(matriz):
    contador = 0
    for fila in range(len(matriz)):
        for colum in range(len(matriz[0])):
            if matriz[fila][colum] == 0:
                contador += 1
    return contador

if __name__ == "__main__":
    print(contador_de_ceros([[0,1,0],[2,3,4]]))  # 2
    print(contador_de_ceros([[1,2],[3,4]]))      # 0
