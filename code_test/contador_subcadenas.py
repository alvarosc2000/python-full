def isVocal(letra):
    return letra in "aeiou"

def solution(pattern, source):
    if source == "":
        return 0
    
    contador = 0
    largo = len(pattern)
    
    for i in range(len(source) - largo + 1):
        cumple = True
        
        for j in range(largo):
            if pattern[j] == '0' and not isVocal(source[i + j]):
                cumple = False
                break
            if pattern[j] == '1' and isVocal(source[i + j]):
                cumple = False
                break
        
        if cumple:
            contador += 1
    
    return contador
