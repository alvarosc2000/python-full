def solution(nums, k):
    suma = 0
    max_len = 0
    memoria = {0:-1}

    for i, elem in enumerate(nums):
        suma += elem
        if suma - k in memoria:
            max_len = max(max_len, i-memoria[suma-k])
        
        if suma not in memoria:
            memoria[suma] = elem
        
        return max_len
    

print(solution([1,2,1,1,1], 3))