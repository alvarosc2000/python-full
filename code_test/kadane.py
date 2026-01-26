def solutions(nums):
    
    max_actual = max_total = nums[0]
    
    for elem in nums[1:]:
        max_actual = max(elem, max_actual + elem)
        max_total = max(max_actual,max_total)

    return max_total

print(solutions([-2,1,-3,4,-1,2,1,-5,4]))