def sumaMaxima(array):
    max_total = maximo_actual = array[0]

    for i in array[1:]:
        maximo_actual = max(i, maximo_actual+i)
        max_total = max(max_total, maximo_actual)
    
    return max_total

print(sumaMaxima([-2,1,-3,4,-1,2,1,-5,4]))