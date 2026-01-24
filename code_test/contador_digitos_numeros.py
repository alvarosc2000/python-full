def contador_letras_digitos_extras():
    cadena = input("Introduce cadena: ")

    contador_letras = 0
    contador_digitos = 0
    contador_extras = 0

    for c in cadena:
        if c.isalpha():
            contador_letras += 1
        elif c.isdigit():
            contador_digitos += 1
        else:
            contador_extras += 1

    return contador_letras, contador_digitos, contador_extras


# --- PRUEBA LOCAL ---
if __name__ == "__main__":
    letras, digitos, extras = contador_letras_digitos_extras()
    print(f"Letras: {letras}")
    print(f"Dígitos: {digitos}")
    print(f"Extras: {extras}")
