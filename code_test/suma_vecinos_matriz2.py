def sumaV(matriz):
    lista = []
    for f in range(len(matriz)):
        for c in range(len(matriz[0])):
            suma = 0
            if f > 0:
                suma += matriz[f-1][c]
            if c > 0:
                suma += matriz[f][c-1]
            if f < len(matriz)-1:
                suma += matriz[f+1][c]
            if c < len(matriz[0])-1:
                suma += matriz[f][c+1]
            
            lista.append(suma)
    return lista


matrix = [
 [1,2,3],
 [4,5,6],
 [7,8,9]
]

print(sumaV(matrix))