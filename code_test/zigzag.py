def zigzag(nums):
    for indice in range(1,len(nums)-1):
        if nums[indice-1] < nums[indice] and nums[indice] > nums[indice+1]:
            return True
        elif nums[indice-1] > nums[indice] and nums[indice] < nums[indice+1]:
            return True
        else:
            return False

print(zigzag([1, 3, 2, 4, 3]))  # [True, True, True]
print(zigzag([1, 2, 3, 4]))     # [False, False]
print(zigzag([3, 1, 4, 2]))     # [True, True]