def contador_letras_mayusculas(cadena):
    cadena_original_minusculas = cadena.lower()
    cadena_original = cadena

    contador = 0

    for i in range(len(cadena_original)):
        if cadena_original[i] != cadena_original_minusculas[i]:
            contador += 1
    return contador


print(contador_letras_mayusculas("Hola Mundo"))
print(contador_letras_mayusculas("python"))
print(contador_letras_mayusculas(""))

 