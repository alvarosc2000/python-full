def sumaMax(nums):
    if not nums:
        return 0
    
    maxima_act = maxima_total = nums[0]

    for elem in (nums[1:]):
        maxima_act = max(elem, maxima_act+elem)
        maxima_total = max(maxima_act,maxima_total)
    return maxima_total

print(sumaMax([-2,1,-3,4,-1,2,1,-5,4]))  # 6
print(sumaMax([1,2,3,4]))               # 10