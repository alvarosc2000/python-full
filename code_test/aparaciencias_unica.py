def valores_unicos_posicion(nums):
    lista = []

    if nums == []:
        return []

    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            lista.append(nums[i])
    return lista


# --- TESTS ---
print(valores_unicos_posicion([2,3,2,4,5,5,6]))      # [3,4,6]
print(valores_unicos_posicion([1,1,1,1]))            # []
print(valores_unicos_posicion([]))                   # []
print(valores_unicos_posicion([0,-1,0,2]))           # [-1,2]
