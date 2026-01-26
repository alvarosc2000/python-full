def suma_vecinos(matriz):
    resultado = []
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            suma = 0
            if fila > 0:
                suma += matriz[fila-1][columna]
            if columna > 0:
                suma += matriz[fila][columna-1]
            if fila < len(matriz)-1:
                suma += matriz[fila+1][columna]
            if columna < len(matriz[0])-1:
                suma += matriz[fila][columna+1]
            resultado.append(suma)
    
    return resultado

# Pruebas
mat = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]
print(suma_vecinos(mat))  # [6,9,8,12,20,14,12,17,14]