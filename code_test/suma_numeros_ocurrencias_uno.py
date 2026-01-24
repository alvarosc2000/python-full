def sumaNumeros(nums):
    suma = 0
    for i in range(len(nums)):
       if (nums.count(nums[i]) == 1):
           suma += nums[i]
    return suma

print(sumaNumeros([11,2,3,4,5,4,3,2,1,2,6]))

