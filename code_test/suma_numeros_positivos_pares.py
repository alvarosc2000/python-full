def solutions(nums):
    suma = 0

    for elem in nums:
        if elem > 0 and elem % 2 == 0:
            suma += elem
    return suma


print(solutions([1, 2, -4, 6, 3]))
print(solutions([-1, -3, 5]))
print(solutions([]))
