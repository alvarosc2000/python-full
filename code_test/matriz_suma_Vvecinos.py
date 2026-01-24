def suma_vecinos(matriz, i, j):
    """
    Devuelve la suma de los vecinos válidos
    (arriba, abajo, izquierda, derecha) de la posición (i,j)
    """
    suma = 0
    filas = len(matriz)
    if filas == 0:
        return 0
    columnas = len(matriz[0])

    # Vecino arriba
    if i > 0:
        suma += matriz[i-1][j]
    # Vecino abajo
    if i < filas - 1:
        suma += matriz[i+1][j]
    # Vecino izquierda
    if j > 0:
        suma += matriz[i][j-1]
    # Vecino derecha
    if j < columnas - 1:
        suma += matriz[i][j+1]

    return suma

# --- PRUEBAS LOCALES ---
if __name__ == "__main__":
    mat = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    # Posición en el medio
    print(suma_vecinos(mat, 1, 1))  # 20

    # Esquina superior izquierda
    print(suma_vecinos(mat, 0, 0))  # 6

    # Esquina inferior derecha
    print(suma_vecinos(mat, 2, 2))  # 14

    # Borde izquierdo, fila 1
    print(suma_vecinos(mat, 1, 0))  # 13
