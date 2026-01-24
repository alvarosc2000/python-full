def matrizSumaFilas(matrix):
    lista = []
    for fila in matrix:
        suma_fila = 0
        for elem in fila:
            suma_fila += elem
        lista.append(suma_fila)

    return lista

if __name__ == "__main__":
    print(matrizSumaFilas([[1, 2], [3, 4], [5, 6]]))  # [3, 7, 11]
    print(matrizSumaFilas([[0, 0]]))                  # [0]
