def numero_no_rep(nums):
    lista_no_repetido = []
    lista_repetidos = []

    for i in range(len(nums)):
        if nums[i] not in lista_no_repetido and nums.count(nums[i]) == 1:
            lista_no_repetido.append(nums[i])
        elif nums[i] not in lista_repetidos and nums.count(nums[i]) > 1:
            lista_repetidos.append(nums[i])
        

    return lista_repetidos, lista_no_repetido

(r,nr) = numero_no_rep([2,3,5,2,5,7,4,6,8])
print(f"Los repetidos {r} y los no repetidos {nr}")