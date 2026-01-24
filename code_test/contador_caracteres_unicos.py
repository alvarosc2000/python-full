def solution(nums):
    freq = {}
    for x in nums:
        freq[x] = freq.get(x, 0) + 1

    contador = 0
    for x in freq:
        if freq[x] == 1:
            contador += 1

    return contador
