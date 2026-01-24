def rotar_matriz_90(matriz):
    """
    Dada una matriz cuadrada n x n, devuelve la matriz rotada 90° en sentido horario.
    """
    if not matriz or not matriz[0]:
        return []

    for fila in range(len(matriz)):
        for col in range(fila, len(matriz)):
            matriz[fila][col], matriz[col][fila] = matriz[col][fila],matriz[fila][col]
    
    for row in matriz:
        row.reverse()
    return matriz

# --- PRUEBAS LOCALES ---
if __name__ == "__main__":
    matriz1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(rotar_matriz_90(matriz1))
    # Esperado: [[7,4,1],[8,5,2],[9,6,3]]

    matriz2 = [
        [1, 2],
        [3, 4]
    ]
    print(rotar_matriz_90(matriz2))
    # Esperado: [[3,1],[4,2]]

    matriz3 = [
        [1]
    ]
    print(rotar_matriz_90(matriz3))
    # Esperado: [[1]]

    matriz4 = []
    print(rotar_matriz_90(matriz4))
    # Esperado: []
