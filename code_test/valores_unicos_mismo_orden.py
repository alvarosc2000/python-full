def valores_unicos(nums):
    cadena = []

    for i in range(len(nums)):
        if nums.count(nums[i]) == 1:
            cadena.append(nums[i])
    
    return cadena

print(valores_unicos([1,2,3,2,4,3,5]))  # [1,4,5]
print(valores_unicos([1,1,2,2]))        # []