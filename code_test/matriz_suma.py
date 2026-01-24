def sumaMatriz(matriz):
    suma = 0
    for col in range(len(matriz[0])):
        for fila in range(len(matriz)):
            suma += matriz[fila][col]
    return suma

if __name__ == "__main__":
    print(sumaMatriz([[1, 2], [3, 4]]))          # 10
    print(sumaMatriz([[0, 0], [0, 0]]))          # 0
    print(sumaMatriz([[-1, 2], [3, -4]]))        # 0
