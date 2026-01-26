def matriz_escalonada(matriz):
    for fila in range(len(matriz)):
        for col in range(len(matriz[0])):
            if col > fila and matriz[fila][col] != 0:
                return False
    return True

    
print(matriz_escalonada([[1,2,0],
 [0,3,4],
 [0,0,5]]))