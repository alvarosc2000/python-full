def sumaMatriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    resultado = []

    for fila in range(filas):
        for columna in range(columnas):
            suma = 0
            # vecinos verticales y horizontales
            if fila > 0:
                suma += matriz[fila-1][columna]       # arriba
            if fila < filas-1:
                suma += matriz[fila+1][columna]       # abajo
            if columna > 0:
                suma += matriz[fila][columna-1]       # izquierda
            if columna < columnas-1:
                suma += matriz[fila][columna+1]       # derecha
            
            # vecinos diagonales
            if fila > 0 and columna > 0:
                suma += matriz[fila-1][columna-1]     # arriba-izquierda
            if fila > 0 and columna < columnas-1:
                suma += matriz[fila-1][columna+1]     # arriba-derecha
            if fila < filas-1 and columna > 0:
                suma += matriz[fila+1][columna-1]     # abajo-izquierda
            if fila < filas-1 and columna < columnas-1:
                suma += matriz[fila+1][columna+1]     # abajo-derecha
            
            resultado.append(suma)

    return resultado

# --- Test ---
mat = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

print(sumaMatriz(mat))
