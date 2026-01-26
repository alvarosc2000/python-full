def sumaD(matriz):
    suma1 = 0
    suma2 = 0

    for fila in range(len(matriz)):
        for col in range(len(matriz[fila])):
            if fila == col:
                suma1 += matriz[fila][col]
            
            if fila + col == len(matriz)-1:
                suma2 += matriz[fila][col]
        
    return suma1 , suma2

(s1,s2) = sumaD([
 [1,2,3],
 [4,5,6],
 [7,8,9]
])

print(f"la suma 1 es {s1} y la 2 es {s2}")