def contador_cadena(cadena):
    contador_digitos = 0
    contador_letras = 0
    contador_extras = 0

    cadena_aux = cadena.lower()

    for i in range(len(cadena_aux)):
        if cadena_aux[i].isdigit():
            contador_digitos += 1
        elif cadena_aux[i].isalpha():
            contador_letras += 1
        else:
            contador_extras += 1
    
    return contador_extras, contador_digitos, contador_letras

(e,d,l) = contador_cadena("Hola")
print(f"Extras: {e}, Digitos: {d}, Letras: {l}")
