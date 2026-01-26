def elementos_diagonal(matriz):
    elementos = []

    for fila in range(len(matriz)):
        for col in range(len(matriz[0])):
            if fila == col:
                elementos.append(matriz[fila][col])
    return elementos

if __name__ == "__main__":
    print(elementos_diagonal([[1,2,3],[4,5,6],[7,8,9]]))  # [1, 5, 9]
    print(elementos_diagonal([[5]]))                      # [5]
