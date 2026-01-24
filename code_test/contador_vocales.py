def isVocal(letra):
    vocales = "aeiou"
    if letra not in vocales:
        return False
    return True

def solution(s):
    contador_vocales = 0
    contador_consonantes = 0
    contador_caracteres_esp = 0
    cadena_aux = s.lower()
    for i in range(len(cadena_aux)):
        if cadena_aux[i].isalpha() and isVocal(cadena_aux[i]):
            contador_vocales += 1
        elif cadena_aux[i].isalpha() and not isVocal(cadena_aux[i]):
            contador_consonantes += 1
        else:
            contador_caracteres_esp += 1

    return contador_vocales, contador_consonantes, contador_caracteres_esp


# --- PRUEBA LOCAL ---
if __name__ == "__main__":
    s = "Hola 123!! Mundo"
    print("Resultado esperado: 4,5,7")
    print("Resultado obtenido:", solution(s))
