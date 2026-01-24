def solution(nums):
    suma = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            suma += nums[i]
    return suma


# --- PRUEBAS LOCALES (NO VAN EN CODESIGNAL) ---
if __name__ == "__main__":
    print(solution([1, -2, 3, 0, 5]))   # esperado: 9
    print(solution([-1, -2, -3]))       # esperado: 0
    print(solution([]))                 # esperado: 0
