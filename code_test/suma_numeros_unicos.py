def suma_unicos(nums):
    suma = 0
    for elem in range(len(nums)):
        if nums.count(nums[elem]) == 1:
            suma += nums[elem]
    return suma

# --- TESTS ---
print(suma_unicos([1,2,3,4,5,4,3,2,1,6]))  # 11
print(suma_unicos([11,22,11,33,44,44]))    # 22 + 33 = 55
