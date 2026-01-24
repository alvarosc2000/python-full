def suma_numeros_pares(cadena):
    suma = 0
    for elem in cadena:
        if elem % 2 == 0 and elem > 0:
            suma += elem
    return suma

print(suma_numeros_pares([1,3,-2,3,5,6,-2,-6]))