def maximo_columnas(matriz):
    if not matriz or not matriz[0]:
        return []
    
    n_col = len(matriz[0])
    maximos = []

    for col in range(n_col):
        mayor = matriz[0][col]
        for fila in range(1, len(matriz)):
            if matriz[fila][col] > mayor:
                mayor = matriz[fila][col]
        maximos.append(mayor)
    
    return maximos

# --- PRUEBAS ---
if __name__ == "__main__":
    print(maximo_columnas([[1,5,3],[4,2,6]]))  # [4,5,6]
    print(maximo_columnas([[7],[3],[9]]))      # [9]
    print(maximo_columnas([]))                  # []
    print(maximo_columnas([[1,2,3]]))           # [1,2,3]
