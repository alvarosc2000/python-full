def suma_maxima(nums):
    maxima_actual = maxima_total = nums[0]

    for n in nums[1:]:
        maxima_actual = max(n, maxima_actual+n)
        maxima_total = max(maxima_actual, maxima_total)
    return maxima_total

print(suma_maxima([-2,1,-3,4,-1,2,1,-5,4]))