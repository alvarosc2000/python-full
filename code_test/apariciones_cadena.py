from collections import Counter

def apariciones(cadena):
    conteos = Counter(cadena)
    print(dict(conteos))

apariciones([1,2,3,4,2,3,5,6,3,2,5,6,36])    