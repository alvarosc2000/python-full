def contar_ocurrencias(nums):
    contador = {}

    for elem in nums:
        if elem in contador:
            contador[elem] += 1
        else:
            contador[elem] = 1
    
    return contador

print(contar_ocurrencias([1,2,2,3,3,3]))  # {1:1,2:2,3:3}
print(contar_ocurrencias([5,5,5,5]))      # {5:4}