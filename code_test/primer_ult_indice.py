def indice_elem(nums,v):
    indice_1 = -1
    indice_2 = -1

    for elem in range(0, len(nums)-1):
        if nums[elem] == v and indice_1 == -1:
            indice_1 = elem
    
    for elem in range(len(nums)-1,-1,-1):
        if nums[elem] == v and indice_1 != -1 and indice_2 == -1:
            indice_2 = elem

    return indice_1, indice_2

(i1,i2) = indice_elem([1,2,3],5)
print(f"La primera posicion {i1} y la segunda es {i2}")