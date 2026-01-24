def sumaDiagonal(matrix):
    suma = 0
    for fila in range(len(matrix)):
        for colum in range(len(matrix[0])):
            if fila == colum:
                suma += matrix[fila][colum]
    return suma

if __name__ == "__main__":
    print(sumaDiagonal([[1,2,3],[4,5,6],[7,8,9]]))  # [1, 5, 9]
    print(sumaDiagonal([[5]]))                      # [5]
