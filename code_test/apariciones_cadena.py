from collections import Counter

def apariciones(nums):
    dicc = {}

    for elem in nums:
        if elem in dicc:
            dicc[elem] += 1
        else:
            dicc[elem] = 1

    return dicc

print(apariciones([1,2,3,4,2,3,5,6,3,2,5,6,36]))    