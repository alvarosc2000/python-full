def solution(s):
    contador = 0
    for c in s:
        if c.isalpha():
            contador += 1
    return contador


# --- PRUEBA LOCAL ---
if __name__ == "__main__":
    s = "Hola 123!! Mundo"
    print("Resultado esperado: 9")
    print("Resultado obtenido:", solution(s))
