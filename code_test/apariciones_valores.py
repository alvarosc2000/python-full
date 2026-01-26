def aparciones(cadena):
    dicc = {}

    for elem in cadena:
        if elem in dicc:
            dicc[elem] += 1
        else:
            dicc[elem] = 1
    
    return dicc


print(aparciones([1,1,3,2,2,3,2,5,6,5]))