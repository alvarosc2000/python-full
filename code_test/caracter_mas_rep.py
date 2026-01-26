def solutions(palabra):
    caracter = ""
    maximo_ocurrencias = 0

    for elem in range(len(palabra)):
        if palabra.count(palabra[elem]) > maximo_ocurrencias:
            caracter = ""
            maximo_ocurrencias = palabra.count(palabra[elem])
            caracter += palabra[elem]
        
    return caracter, maximo_ocurrencias


(c,m) = solutions("abracccccccccccccccccccccccccccccccccccccacccccccccccccccccccdrrrrrrrrra")
print(f"El caracter {c} se repite {m} veces")