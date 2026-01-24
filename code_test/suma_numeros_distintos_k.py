def solution(nums, k):
    for i in range(len(nums)-1):
        if nums[i] + nums[i+1] == k:
            return True
    return False


# --- PRUEBAS LOCALES ---
if __name__ == "__main__":
    print(solution([1, 2, 3, 4], 5))   # True
    print(solution([1, 1, 3], 2))      # True
    print(solution([1, 2, 3], 10))     # False
