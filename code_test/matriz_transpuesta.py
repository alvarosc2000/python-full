def matriz_transpuesta(matriz):
    if not matriz or not matriz[0]:
        return []    
    
    transpuesta = []
    for col in range(len(matriz[0])):
        nueva_fila = []
        for fila in range(len(matriz)):
            nueva_fila.append(matriz[fila][col])
        transpuesta.append(nueva_fila)

    return transpuesta

if __name__ == "__main__":
    print(matriz_transpuesta([[1,2,3],[4,5,6]]))  
    # [[1,4],[2,5],[3,6]]

    print(matriz_transpuesta([[1]]))  
    # [[1]]

    print(matriz_transpuesta([]))  
    # []
