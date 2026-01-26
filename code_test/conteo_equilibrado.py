def solution(s):
    contador_d = 0
    contador_l = 0

    for elem in range(len(s)):
        if s[elem].isdigit():
            contador_d +=1
        else:
            contador_l += 1
    
    if contador_l == contador_d:
        return True
    else:
        return False
    

print(solution("a1b12"))