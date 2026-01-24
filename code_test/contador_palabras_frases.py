def contador_palabras(cadena):
    cad_aux = cadena.split()
    total = len(cad_aux)
    return total

print(contador_palabras("Hola mundo desde Python"))